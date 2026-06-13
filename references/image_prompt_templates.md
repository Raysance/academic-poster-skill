# AI Image Prompt Templates

Use progressive disclosure for image style requirements: start from this routing index, then read only the one prompt template file that matches the figure being generated. Do not load every image style template by default.

## Routing table

| Figure need | Read this file | Use when |
|---|---|---|
| Top-tier CS/ML paper framework figure | `references/image_prompts/cs_pipeline_diagram.md` | Method diagrams with encoder stacks, optimization loops, probability notation, objective functions, or conference-paper vector aesthetics |
| Claymorphic workflow / demo timeline | `references/image_prompts/claymorphic_workflow_demo.md` | Presentation-friendly process timelines, robotics demos, physical-system demos, project workflows, or 3D card-based explanatory figures |

## Selection rules

- Use Python first for any exact data, statistics, plotted values, tables, or quantitative chart geometry.
- Use AI image generation for conceptual diagrams, workflow visuals, mechanism illustrations, polished schematics, and visual packaging.
- If a figure mixes real data with AI visuals, generate or validate the data with Python first; let AI only style the non-numeric visual shell.
- Save prompts and outputs under `poster_work/assets/ai_images/`, but keep prompt/model/API details out of the final poster.
- If none of the routed templates fit, write a project-specific prompt using the approved outline and the general poster visual rules in `SKILL.md`.
