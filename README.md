# Codex Agency Skills

Curated Codex-native skills translated from [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents).

This repository packages reusable `SKILL.md` folders that Codex can discover and use across projects.

## Included Skills

- `agency-ai-data-remediation-engineer`
- `agency-ai-engineer`
- `agency-api-tester`
- `agency-backend-architect`
- `agency-code-reviewer`
- `agency-data-engineer`
- `agency-database-optimizer`
- `agency-devops-automator`
- `agency-frontend-developer`
- `agency-performance-benchmarker`
- `agency-product-manager`
- `agency-rapid-prototyper`
- `agency-reality-checker`
- `agency-security-engineer`
- `agency-software-architect`
- `agency-sprint-prioritizer`
- `agency-technical-writer`
- `agency-ui-designer`
- `agency-ux-researcher`

### Marketing workflow skills

- `marketing-autoresearch`
- `marketing-content-ops`
- `marketing-conversion-ops`
- `marketing-deck-generator`
- `marketing-finance-ops`
- `marketing-growth-engine`
- `marketing-outbound-engine`
- `marketing-podcast-ops`
- `marketing-revenue-intelligence`
- `marketing-sales-pipeline`
- `marketing-sales-playbook`
- `marketing-seo-ops`
- `marketing-team-ops`
- `marketing-x-longform-post`
- `marketing-yt-competitive-analysis`

## Install With Codex Skill Installer

Install one skill:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo hibra984/codex-agency-skills \
  --path skills/agency-frontend-developer
```

Install the full curated pack:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo hibra984/codex-agency-skills \
  --path skills/agency-ai-data-remediation-engineer \
         skills/agency-ai-engineer \
         skills/agency-api-tester \
         skills/agency-backend-architect \
         skills/agency-code-reviewer \
         skills/agency-data-engineer \
         skills/agency-database-optimizer \
         skills/agency-devops-automator \
         skills/agency-frontend-developer \
         skills/agency-performance-benchmarker \
         skills/agency-product-manager \
         skills/agency-rapid-prototyper \
         skills/agency-reality-checker \
         skills/agency-security-engineer \
         skills/agency-software-architect \
         skills/agency-sprint-prioritizer \
         skills/agency-technical-writer \
         skills/agency-ui-designer \
         skills/agency-ux-researcher
```

Install a marketing workflow skill:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo hibra984/codex-agency-skills \
  --path skills/marketing-growth-engine
```

Bulk-import or refresh the upstream marketing pack locally:

```bash
python tools/import_ai_marketing_skills.py \
  --source ../ai-marketing-skills \
  --dest .
```

Restart Codex after installation so new skills are discovered.

## Repository Layout

Each skill lives under `skills/<skill-name>/` and includes:

- `SKILL.md`
- `agents/openai.yaml`

## Contributing

Contributions are welcome through issues and pull requests.

Suggested workflow:

1. Add or refine a skill folder under `skills/`.
2. Keep `SKILL.md` concise and trigger-oriented.
3. Preserve attribution to the original Agency role when adapting source material.
4. Validate skills locally with Codex's `quick_validate.py` before opening a PR.
5. For upstream marketing refreshes, regenerate via `tools/import_ai_marketing_skills.py` instead of editing generated skills by hand.

## Attribution

These skills are adapted from the MIT-licensed [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) and [`ericosiu/ai-marketing-skills`](https://github.com/ericosiu/ai-marketing-skills) projects.

They are translations into Codex skill format, not official upstream artifacts.
