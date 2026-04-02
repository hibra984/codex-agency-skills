# Codex Agency Skills

Curated Codex-native skills translated from [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents).

This repository packages a high-value subset of Agency roles into reusable `SKILL.md` folders that Codex can discover and use across projects.

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

## Attribution

These skills are adapted from the MIT-licensed [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) project.

They are translations into Codex skill format, not official upstream artifacts.
