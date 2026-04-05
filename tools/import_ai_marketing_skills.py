from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


EXCLUDED_SKILL_DIRS = {"eval", "security", "telemetry"}
TEXT_EXTENSIONS = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".sh"}
IGNORE_NAMES = {".git", "__pycache__", ".DS_Store", ".gitignore"}


def normalize_slug(name: str) -> str:
    return re.sub(r"-{2,}", "-", re.sub(r"[^a-z0-9]+", "-", name.lower())).strip("-")


def infer_title(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    return match.group(1).strip() if match else fallback.replace("-", " ").title()


def strip_preamble(markdown: str) -> str:
    text = markdown
    text = re.sub(r"^---\n.*?\n---\n+", "", text, flags=re.DOTALL)
    text = re.sub(r"## Preamble \(runs on skill start\).*?---\n+", "", text, flags=re.DOTALL)
    text = re.sub(r"> \*\*Privacy:.*?\n+", "", text)
    return text


def infer_summary(markdown: str, fallback: str) -> str:
    text = strip_preamble(markdown)
    lines = [line.strip() for line in text.splitlines()]
    for index, line in enumerate(lines):
      if not line or line.startswith("#") or line.startswith("```") or line.startswith("|") or line.startswith("- "):
        continue
      if line.startswith(">"):
        continue
      if line == "---":
        continue
      return line
    return fallback


def infer_use_cases(markdown: str) -> list[str]:
    patterns = [
        r"## When to Use\s+(.*?)(?=\n## |\Z)",
        r"Use this skill when:\s*(.*?)(?=\n## |\n### |\nDo NOT use|\Z)",
        r"## Usage\s+(.*?)(?=\n## |\Z)",
    ]
    for pattern in patterns:
        match = re.search(pattern, markdown, flags=re.DOTALL)
        if not match:
            continue
        bullets = re.findall(r"^\s*[-*]\s+(.+)$", match.group(1), flags=re.MULTILINE)
        cleaned = [re.sub(r"\s+", " ", bullet).strip().rstrip(".") for bullet in bullets if bullet.strip()]
        if cleaned:
            return cleaned[:6]
    return []


def copy_tree_filtered(source: Path, dest: Path, known_slugs: set[str]) -> list[str]:
    copied: list[str] = []
    for item in source.rglob("*"):
        rel = item.relative_to(source)
        if any(part in IGNORE_NAMES for part in rel.parts):
            continue
        if item.is_dir():
            continue
        if rel.as_posix() == "SKILL.md":
            continue
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)
        if target.suffix.lower() in TEXT_EXTENSIONS:
            text = target.read_text(encoding="utf-8", errors="ignore")
            for slug in known_slugs:
                text = text.replace(f"../{slug}/", f"../marketing-{slug}/")
                text = text.replace(f"./{slug}/", f"./marketing-{slug}/")
            target.write_text(text, encoding="utf-8")
        copied.append(rel.as_posix())
    return copied


def write_skill_files(skill_dir: Path, *, slug: str, title: str, summary: str, use_cases: list[str], source_path: str) -> None:
    description = (
        f"Codex-native marketing skill adapted from `{source_path}`. "
        f"Use when {summary[0].lower() + summary[1:] if summary else 'running this workflow'}"
    )
    title_yaml = json.dumps(title)
    summary_yaml = json.dumps(summary)
    prompt_yaml = json.dumps(f"Use the {title} skill to run or adapt this marketing workflow.")
    description_block = "\n".join([f"  {line}" for line in [description]])
    use_case_lines = "\n".join([f"- {item}" for item in use_cases]) if use_cases else "- the user needs this workflow executed or adapted"
    skill_md = f"""---
name: marketing-{slug}
description: >-
{description_block}
---

Adopt the specialist lens of the upstream `{slug}` marketing workflow.

Keep the work practical, execution-oriented, and grounded in measurable marketing outcomes.

Source adapted from `ericosiu/ai-marketing-skills/{slug}/SKILL.md`.

## When to use
{use_case_lines}

## Operating guidance
- Prefer the bundled local scripts, references, and assets in this skill folder over recreating the workflow from scratch.
- Treat upstream Claude instructions as source material; adapt them to Codex and the user's actual codebase or campaign context.
- Skip telemetry, opt-in tracking, and non-local repo setup unless the user explicitly asks for them.
- Preserve concrete scoring models, heuristics, and review checklists when they materially improve output quality.
- Be explicit about required inputs, dependencies, and any external credentials before invoking bundled scripts.
"""
    openai_yaml = f"""interface:
  display_name: {title_yaml}
  short_description: {summary_yaml}
  default_prompt: {prompt_yaml}
"""
    (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")
    agent_dir = skill_dir / "agents"
    agent_dir.mkdir(parents=True, exist_ok=True)
    (agent_dir / "openai.yaml").write_text(openai_yaml, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Import Claude marketing skills into codex-agency-skills.")
    parser.add_argument("--source", required=True, help="Path to the cloned ai-marketing-skills repo")
    parser.add_argument("--dest", default=".", help="Path to codex-agency-skills repo root")
    args = parser.parse_args()

    source_root = Path(args.source).resolve()
    dest_root = Path(args.dest).resolve()
    skills_root = dest_root / "skills"
    skills_root.mkdir(parents=True, exist_ok=True)

    source_dirs = sorted(
        path for path in source_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").exists() and path.name not in EXCLUDED_SKILL_DIRS
    )
    known_slugs = {path.name for path in source_dirs}

    source_commit = "unknown"
    try:
        source_commit = subprocess.check_output(
            ["git", "-c", f"safe.directory={source_root.as_posix()}", "-C", str(source_root), "rev-parse", "HEAD"],
            text=True,
        ).strip()
    except Exception:
        pass

    manifest_entries = []
    for source_dir in source_dirs:
        slug = normalize_slug(source_dir.name)
        target_dir = skills_root / f"marketing-{slug}"
        if target_dir.exists():
            shutil.rmtree(target_dir)
        target_dir.mkdir(parents=True, exist_ok=True)

        upstream_text = (source_dir / "SKILL.md").read_text(encoding="utf-8", errors="ignore")
        title = infer_title(upstream_text, slug)
        summary = infer_summary(upstream_text, f"Run the {title} workflow.")
        use_cases = infer_use_cases(upstream_text)
        write_skill_files(
            target_dir,
            slug=slug,
            title=title,
            summary=summary,
            use_cases=use_cases,
            source_path=f"{source_dir.name}/SKILL.md",
        )

        copied_paths = copy_tree_filtered(source_dir, target_dir, known_slugs)
        manifest = {
            "upstream_repo": "https://github.com/ericosiu/ai-marketing-skills",
            "upstream_commit": source_commit,
            "upstream_path": source_dir.name,
            "local_skill": f"marketing-{slug}",
            "copied_paths": copied_paths,
        }
        (target_dir / "import_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        manifest_entries.append(manifest)

    top_manifest = {
        "upstream_repo": "https://github.com/ericosiu/ai-marketing-skills",
        "upstream_commit": source_commit,
        "imported_skills": manifest_entries,
        "omitted_dirs": ["eval", "security", "telemetry"],
    }
    (dest_root / "tools" / "imported_ai_marketing_skills.json").write_text(
        json.dumps(top_manifest, indent=2),
        encoding="utf-8",
    )
    print(f"Imported {len(manifest_entries)} marketing skills from {source_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
