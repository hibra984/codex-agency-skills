---
name: marketing-outbound-engine
description: >-
  Codex-native marketing skill adapted from `outbound-engine/SKILL.md`. Use when ask the user:
---

Adopt the specialist lens of the upstream `outbound-engine` marketing workflow.

Keep the work practical, execution-oriented, and grounded in measurable marketing outcomes.

Source adapted from `ericosiu/ai-marketing-skills/outbound-engine/SKILL.md`.

## When to use
- the user needs this workflow executed or adapted

## Operating guidance
- Prefer the bundled local scripts, references, and assets in this skill folder over recreating the workflow from scratch.
- Treat upstream Claude instructions as source material; adapt them to Codex and the user's actual codebase or campaign context.
- Skip telemetry, opt-in tracking, and non-local repo setup unless the user explicitly asks for them.
- Preserve concrete scoring models, heuristics, and review checklists when they materially improve output quality.
- Be explicit about required inputs, dependencies, and any external credentials before invoking bundled scripts.
