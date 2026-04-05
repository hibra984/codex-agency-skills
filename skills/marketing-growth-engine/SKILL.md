---
name: marketing-growth-engine
description: >-
  Codex-native marketing skill adapted from `growth-engine/SKILL.md`. Use when autonomous growth experimentation framework based on Karpathy's autoresearch pattern applied to marketing. Creates experiments with hypotheses, logs data points, runs statistical analysis (bootstrap CI + Mann-Whitney U), auto-promotes winners to a living playbook, and suggests next experiments. Supports batch mode (up to 10 variants simultaneously).
---

Adopt the specialist lens of the upstream `growth-engine` marketing workflow.

Keep the work practical, execution-oriented, and grounded in measurable marketing outcomes.

Source adapted from `ericosiu/ai-marketing-skills/growth-engine/SKILL.md`.

## When to use
- Creating or managing A/B or multivariate experiments for any marketing channel
- Logging experiment data points after content is published or campaigns run
- Scoring experiments to determine statistical winners
- Checking the playbook for proven best practices before creating new content
- Generating weekly scorecards across all channels
- Monitoring campaign pacing and health

## Operating guidance
- Prefer the bundled local scripts, references, and assets in this skill folder over recreating the workflow from scratch.
- Treat upstream Claude instructions as source material; adapt them to Codex and the user's actual codebase or campaign context.
- Skip telemetry, opt-in tracking, and non-local repo setup unless the user explicitly asks for them.
- Preserve concrete scoring models, heuristics, and review checklists when they materially improve output quality.
- Be explicit about required inputs, dependencies, and any external credentials before invoking bundled scripts.
