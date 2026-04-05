---
name: marketing-conversion-ops
description: >-
  Codex-native marketing skill adapted from `conversion-ops/SKILL.md`. Use when aI-powered conversion rate optimization: landing page audits, CRO scoring, survey segmentation, and lead magnet generation.
---

Adopt the specialist lens of the upstream `conversion-ops` marketing workflow.

Keep the work practical, execution-oriented, and grounded in measurable marketing outcomes.

Source adapted from `ericosiu/ai-marketing-skills/conversion-ops/SKILL.md`.

## When to use
- User asks for a landing page audit or CRO analysis
- User wants to score a page across conversion dimensions
- User needs to identify conversion bottlenecks on a URL
- User has survey data and wants to segment respondents by pain point
- User wants lead magnet ideas generated from survey responses
- User needs batch CRO analysis across multiple URLs

## Operating guidance
- Prefer the bundled local scripts, references, and assets in this skill folder over recreating the workflow from scratch.
- Treat upstream Claude instructions as source material; adapt them to Codex and the user's actual codebase or campaign context.
- Skip telemetry, opt-in tracking, and non-local repo setup unless the user explicitly asks for them.
- Preserve concrete scoring models, heuristics, and review checklists when they materially improve output quality.
- Be explicit about required inputs, dependencies, and any external credentials before invoking bundled scripts.
