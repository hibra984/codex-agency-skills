---
name: marketing-revenue-intelligence
description: >-
  Codex-native marketing skill adapted from `revenue-intelligence/SKILL.md`. Use when aI-powered revenue intelligence: sales call insight extraction, content-to-revenue attribution, and multi-source client reporting.
---

Adopt the specialist lens of the upstream `revenue-intelligence` marketing workflow.

Keep the work practical, execution-oriented, and grounded in measurable marketing outcomes.

Source adapted from `ericosiu/ai-marketing-skills/revenue-intelligence/SKILL.md`.

## When to use
- User wants to extract insights from Gong sales call transcripts
- User needs to identify objections, buying signals, or competitive mentions in calls
- User wants to prove content ROI by mapping content to closed deals
- User needs revenue attribution across first-touch and multi-touch models
- User wants to generate a unified client report from GA4 + HubSpot + Ahrefs + Gong
- User asks about content gaps in the buyer journey

## Operating guidance
- Prefer the bundled local scripts, references, and assets in this skill folder over recreating the workflow from scratch.
- Treat upstream Claude instructions as source material; adapt them to Codex and the user's actual codebase or campaign context.
- Skip telemetry, opt-in tracking, and non-local repo setup unless the user explicitly asks for them.
- Preserve concrete scoring models, heuristics, and review checklists when they materially improve output quality.
- Be explicit about required inputs, dependencies, and any external credentials before invoking bundled scripts.
