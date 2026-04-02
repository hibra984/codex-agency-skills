from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.request import urlopen


SKILL_CREATOR_DIR = Path(r"C:\Users\hibra\.codex\skills\.system\skill-creator")
INIT_SKILL = SKILL_CREATOR_DIR / "scripts" / "init_skill.py"
VALIDATE_SKILL = SKILL_CREATOR_DIR / "scripts" / "quick_validate.py"


CURATED_SKILLS = [
    {
        "source": "engineering/engineering-ai-engineer.md",
        "slug": "agency-ai-engineer",
        "display_name": "Agency AI Engineer",
        "short_description": "AI engineering specialist from agency-agents.",
        "default_prompt": "Use the Agency AI Engineer skill to design or implement an AI-powered feature.",
        "trigger": (
            "AI engineering skill translated from the agency-agents AI Engineer agent. "
            "Use when building AI-powered features, integrating LLMs or ML models, designing "
            "inference pipelines, handling production AI deployment, or improving AI safety and monitoring."
        ),
    },
    {
        "source": "engineering/engineering-data-engineer.md",
        "slug": "agency-data-engineer",
        "display_name": "Agency Data Engineer",
        "short_description": "Data engineering specialist from agency-agents.",
        "default_prompt": "Use the Agency Data Engineer skill to design or improve a data pipeline or platform.",
        "trigger": (
            "Data engineering skill translated from the agency-agents Data Engineer agent. "
            "Use when designing ETL or ELT pipelines, data lakehouse layers, schemas, data contracts, "
            "streaming systems, observability, or analytics-ready data infrastructure."
        ),
    },
    {
        "source": "engineering/engineering-ai-data-remediation-engineer.md",
        "slug": "agency-ai-data-remediation-engineer",
        "display_name": "Agency AI Data Remediation Engineer",
        "short_description": "AI data remediation specialist from agency-agents.",
        "default_prompt": "Use the Agency AI Data Remediation Engineer skill to design a safe AI-assisted data remediation workflow.",
        "trigger": (
            "AI-assisted data remediation skill translated from the agency-agents AI Data Remediation Engineer agent. "
            "Use when detecting anomaly clusters, generating safe remediation logic, building air-gapped AI repair "
            "flows, or guaranteeing audited zero-data-loss handling for broken data."
        ),
    },
    {
        "source": "engineering/engineering-frontend-developer.md",
        "slug": "agency-frontend-developer",
        "display_name": "Agency Frontend Developer",
        "short_description": "Frontend specialist from agency-agents.",
        "default_prompt": "Use the Agency Frontend Developer skill to build or refactor a modern frontend feature.",
        "trigger": (
            "Specialized frontend implementation skill translated from the agency-agents "
            "Frontend Developer agent. Use when building or refactoring modern web UIs, "
            "component systems, responsive layouts, accessibility improvements, design "
            "implementation, or frontend performance optimization."
        ),
    },
    {
        "source": "engineering/engineering-backend-architect.md",
        "slug": "agency-backend-architect",
        "display_name": "Agency Backend Architect",
        "short_description": "Backend architecture specialist from agency-agents.",
        "default_prompt": "Use the Agency Backend Architect skill to design or improve a backend system.",
        "trigger": (
            "Specialized backend architecture skill translated from the agency-agents "
            "Backend Architect agent. Use when designing APIs, data models, service "
            "boundaries, backend reliability, integrations, or scalable server-side systems."
        ),
    },
    {
        "source": "engineering/engineering-software-architect.md",
        "slug": "agency-software-architect",
        "display_name": "Agency Software Architect",
        "short_description": "System design specialist from agency-agents.",
        "default_prompt": "Use the Agency Software Architect skill to evaluate architecture options and tradeoffs.",
        "trigger": (
            "System design and software architecture skill translated from the agency-agents "
            "Software Architect agent. Use when making architectural decisions, defining "
            "bounded contexts, planning system evolution, or comparing implementation tradeoffs."
        ),
    },
    {
        "source": "engineering/engineering-code-reviewer.md",
        "slug": "agency-code-reviewer",
        "display_name": "Agency Code Reviewer",
        "short_description": "Code review specialist from agency-agents.",
        "default_prompt": "Use the Agency Code Reviewer skill to review this change set for risk and quality.",
        "trigger": (
            "Specialized code review skill translated from the agency-agents Code Reviewer agent. "
            "Use when reviewing diffs, identifying bugs, security issues, maintainability risks, "
            "test gaps, or mentoring through review comments."
        ),
    },
    {
        "source": "engineering/engineering-security-engineer.md",
        "slug": "agency-security-engineer",
        "display_name": "Agency Security Engineer",
        "short_description": "Security specialist from agency-agents.",
        "default_prompt": "Use the Agency Security Engineer skill to assess this design or code for security risks.",
        "trigger": (
            "Application security skill translated from the agency-agents Security Engineer agent. "
            "Use when reviewing authentication, authorization, secrets handling, threat models, "
            "secure defaults, exploit paths, or security controls."
        ),
    },
    {
        "source": "engineering/engineering-database-optimizer.md",
        "slug": "agency-database-optimizer",
        "display_name": "Agency Database Optimizer",
        "short_description": "Database specialist from agency-agents.",
        "default_prompt": "Use the Agency Database Optimizer skill to improve this schema or query path.",
        "trigger": (
            "Database optimization skill translated from the agency-agents Database Optimizer agent. "
            "Use when improving SQL queries, indexes, schema design, migrations, data access paths, "
            "or diagnosing slow database behavior."
        ),
    },
    {
        "source": "engineering/engineering-devops-automator.md",
        "slug": "agency-devops-automator",
        "display_name": "Agency DevOps Automator",
        "short_description": "DevOps specialist from agency-agents.",
        "default_prompt": "Use the Agency DevOps Automator skill to improve this deployment or CI/CD workflow.",
        "trigger": (
            "DevOps and automation skill translated from the agency-agents DevOps Automator agent. "
            "Use when working on CI/CD pipelines, deployments, container workflows, environment "
            "automation, monitoring, or release reliability."
        ),
    },
    {
        "source": "engineering/engineering-rapid-prototyper.md",
        "slug": "agency-rapid-prototyper",
        "display_name": "Agency Rapid Prototyper",
        "short_description": "Rapid prototyping specialist from agency-agents.",
        "default_prompt": "Use the Agency Rapid Prototyper skill to build a fast MVP for this idea.",
        "trigger": (
            "Rapid prototyping skill translated from the agency-agents Rapid Prototyper agent. "
            "Use when building an MVP, proof of concept, hackathon-style feature, or fast validation "
            "artifact where speed and end-to-end usefulness matter."
        ),
    },
    {
        "source": "engineering/engineering-technical-writer.md",
        "slug": "agency-technical-writer",
        "display_name": "Agency Technical Writer",
        "short_description": "Technical writing specialist from agency-agents.",
        "default_prompt": "Use the Agency Technical Writer skill to document this system clearly for developers.",
        "trigger": (
            "Technical writing skill translated from the agency-agents Technical Writer agent. "
            "Use when writing or improving API docs, setup guides, architecture notes, migration "
            "docs, tutorials, or other developer-facing documentation."
        ),
    },
    {
        "source": "design/design-ui-designer.md",
        "slug": "agency-ui-designer",
        "display_name": "Agency UI Designer",
        "short_description": "UI design specialist from agency-agents.",
        "default_prompt": "Use the Agency UI Designer skill to improve the interface and visual system for this feature.",
        "trigger": (
            "UI design system skill translated from the agency-agents UI Designer agent. "
            "Use when creating or refining interface layouts, component libraries, visual hierarchy, "
            "design tokens, or implementation-ready UI direction."
        ),
    },
    {
        "source": "design/design-ux-researcher.md",
        "slug": "agency-ux-researcher",
        "display_name": "Agency UX Researcher",
        "short_description": "UX research specialist from agency-agents.",
        "default_prompt": "Use the Agency UX Researcher skill to analyze this flow for user friction and usability.",
        "trigger": (
            "UX research skill translated from the agency-agents UX Researcher agent. "
            "Use when analyzing user flows, usability issues, behavioral friction, research findings, "
            "interview synthesis, or evidence-based experience improvements."
        ),
    },
    {
        "source": "product/product-manager.md",
        "slug": "agency-product-manager",
        "display_name": "Agency Product Manager",
        "short_description": "Product strategy specialist from agency-agents.",
        "default_prompt": "Use the Agency Product Manager skill to shape this feature into a strong product plan.",
        "trigger": (
            "Product management skill translated from the agency-agents Product Manager agent. "
            "Use when defining requirements, framing outcomes, prioritizing scope, clarifying "
            "product tradeoffs, or turning ideas into actionable plans."
        ),
    },
    {
        "source": "product/product-sprint-prioritizer.md",
        "slug": "agency-sprint-prioritizer",
        "display_name": "Agency Sprint Prioritizer",
        "short_description": "Sprint prioritization specialist from agency-agents.",
        "default_prompt": "Use the Agency Sprint Prioritizer skill to prioritize this backlog or sprint scope.",
        "trigger": (
            "Sprint prioritization skill translated from the agency-agents Sprint Prioritizer agent. "
            "Use when sequencing backlog work, choosing sprint scope, cutting lower-value work, "
            "or aligning delivery with constraints and impact."
        ),
    },
    {
        "source": "testing/testing-api-tester.md",
        "slug": "agency-api-tester",
        "display_name": "Agency API Tester",
        "short_description": "API testing specialist from agency-agents.",
        "default_prompt": "Use the Agency API Tester skill to validate this API behavior and failure handling.",
        "trigger": (
            "API testing skill translated from the agency-agents API Tester agent. "
            "Use when validating endpoints, request and response contracts, authentication behavior, "
            "error handling, or integration reliability."
        ),
    },
    {
        "source": "testing/testing-performance-benchmarker.md",
        "slug": "agency-performance-benchmarker",
        "display_name": "Agency Performance Benchmarker",
        "short_description": "Performance specialist from agency-agents.",
        "default_prompt": "Use the Agency Performance Benchmarker skill to measure and improve performance here.",
        "trigger": (
            "Performance benchmarking skill translated from the agency-agents Performance Benchmarker agent. "
            "Use when measuring throughput, latency, frontend performance, load behavior, regressions, "
            "or performance optimization opportunities."
        ),
    },
    {
        "source": "testing/testing-reality-checker.md",
        "slug": "agency-reality-checker",
        "display_name": "Agency Reality Checker",
        "short_description": "Release-readiness specialist from agency-agents.",
        "default_prompt": "Use the Agency Reality Checker skill to assess whether this is genuinely ready to ship.",
        "trigger": (
            "Release-readiness and reality-check skill translated from the agency-agents Reality Checker agent. "
            "Use when deciding if a feature is production ready, verifying claims with evidence, or "
            "identifying the highest-risk gaps before release."
        ),
    },
]


SECTION_PATTERNS = {
    "Primary focus": r"## 🎯 Your Core Mission(.*?)(?=\n## )",
    "Critical rules": r"## 🚨 Critical Rules You Must Follow(.*?)(?=\n## )",
    "Workflow": r"## 🔄 Your Workflow Process(.*?)(?=\n## )",
    "Deliverables": r"## 📋 Your .*?Deliverables(.*?)(?=\n## )",
    "Communication style": r"## 💭 Your Communication Style(.*?)(?=\n## )",
    "Success metrics": r"## 🎯 Your Success Metrics(.*?)(?=\n## )",
}


def fetch_text(url: str) -> str:
    with urlopen(url) as response:
        return response.read().decode("utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError("Missing frontmatter")
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def extract_section(text: str, pattern: str) -> str:
    match = re.search(pattern, text, re.S)
    if not match:
        return ""
    section = match.group(1).strip()
    section = re.sub(r"```.*?```", "", section, flags=re.S)
    section = re.sub(r"\n{3,}", "\n\n", section)
    return section.strip()


def make_skill_body(agent_name: str, source_path: str, text: str) -> str:
    parts = [
        f"Adopt the specialist lens of the Agency `{agent_name}` role.",
        "",
        "Keep the work practical, deliverable-focused, and evidence-based. Prefer concrete output over generic advice.",
        "",
        f"Source adapted from `msitarzewski/agency-agents/{source_path}`.",
    ]

    for title, pattern in SECTION_PATTERNS.items():
        content = extract_section(text, pattern)
        if not content:
            continue
        parts.extend(["", f"## {title}", content])

    parts.extend(
        [
            "",
            "## Operating guidance",
            "- Stay specialized to this role instead of drifting into generic assistant behavior.",
            "- Favor checklists, concrete recommendations, and implementation-ready outputs.",
            "- Preserve the original role's quality bar, but adapt recommendations to the user's codebase and constraints.",
            "- Escalate tradeoffs clearly when speed, quality, and scope are in tension.",
        ]
    )

    return "\n".join(parts).strip() + "\n"


def write_skill_md(skill_dir: Path, name: str, description: str, body: str) -> None:
    content = f"---\nname: {name}\ndescription: {description}\n---\n\n{body}"
    (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")


def init_skill(dest: Path, spec: dict[str, str]) -> Path:
    args = [
        sys.executable,
        str(INIT_SKILL),
        spec["slug"],
        "--path",
        str(dest),
        "--interface",
        f"display_name={spec['display_name']}",
        "--interface",
        f"short_description={spec['short_description']}",
        "--interface",
        f"default_prompt={spec['default_prompt']}",
    ]
    subprocess.run(args, check=True)
    return dest / spec["slug"]


def validate_skill(skill_dir: Path) -> None:
    subprocess.run([sys.executable, str(VALIDATE_SKILL), str(skill_dir)], check=True)


def install_curated_pack(dest: Path, force: bool) -> list[Path]:
    created: list[Path] = []

    for spec in CURATED_SKILLS:
        source_url = f"https://raw.githubusercontent.com/msitarzewski/agency-agents/main/{spec['source']}"
        text = fetch_text(source_url)
        frontmatter = parse_frontmatter(text)
        skill_dir = dest / spec["slug"]

        if skill_dir.exists():
            if not force:
                print(f"Skipping existing skill: {spec['slug']}")
                continue
            subprocess.run(
                [
                    "powershell",
                    "-NoProfile",
                    "-Command",
                    f"Remove-Item -LiteralPath '{skill_dir}' -Recurse -Force",
                ],
                check=True,
            )

        init_skill(dest, spec)
        body = make_skill_body(frontmatter.get("name", spec["slug"]), spec["source"], text)
        write_skill_md(skill_dir, spec["slug"], spec["trigger"], body)
        validate_skill(skill_dir)
        created.append(skill_dir)
        print(f"Created {spec['slug']}")

    return created


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dest",
        default=str(Path.home() / ".codex" / "skills"),
        help="Destination skills directory",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing generated skills",
    )
    args = parser.parse_args()

    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)

    created = install_curated_pack(dest, args.force)
    print(f"Installed {len(created)} curated Agency skills into {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
