---
name: academic-poster
description: Create publication-quality academic posters from experiment outlines, data, images, author metadata, and user constraints. Use this skill whenever the user asks to make, draft, redesign, typeset, or export a scientific poster in Chinese or English, especially with lab data, experiment plans, LaTeX/PPT requirements, institution branding, logos, or AI image generation details.
---

# Academic Poster

Create polished academic posters in Chinese or English, in PPT/PPTX or LaTeX/PDF. Use AI image generation heavily for poster-ready scientific visuals and chart panels, while using Python to clean data, compute summaries, and verify numbers.

## Inputs to collect

Ask only for missing critical items:

- Engineering setup: AI interface/API, poster size/orientation, language, output format, file paths/folder name, build tools.
- Poster content: title/subtitle, authors, affiliations, institution rules, experiment outline, theory, methods, datasets, results, conclusions, references.
- Existing image assets: logos, experimental images, microscopy, photos, diagrams, QR codes.
- Image generation method; if AI is used, collect API docs, endpoint/model, key handling, image size, and limits.

If the user provides logos or experimental images, ask how each should be used before layout work: title/header logo, affiliation block, experimental schematic input, result panel, background reference, supplemental/QR, or exclude.

## Project folder

Keep all intermediate and final files inside one project subfolder, defaulting to:

```text
poster_work/
  inputs/              # raw outline, data, references, logos, user images
  drafts/              # project_requirements.md, experiment_outline.md, layout_plan.md
  scripts/             # data processing, AI image API wrapper, build scripts
  assets/              # figures, ai_images, templates, logos, user_images
  output/              # poster source and final export
```

## Two approval gates

1. **Project requirements confirmation**
   - Create `poster_work/drafts/project_requirements.md` before any outline, figure, AI image, layout, PPT, LaTeX, or PDF generation.
   - Include only engineering/setup requirements: AI interface/API docs/key handling/model/limits, poster size and orientation, poster language, output format, project file paths/folder name, output locations, build/export tools, and open engineering questions.
   - Do not confirm poster scientific/content details here; put title, authors, affiliations, branding decisions, image-use decisions, scientific story, formulas, workflow, data, results, references, and section content in the second confirmation.
   - Show it to the user and stop. Continue only after explicit approval or requested revisions.

2. **Experiment outline confirmation**
   - After requirements approval, create `poster_work/drafts/experiment_outline.md` and show it to the user. This second confirmation owns all poster content decisions.
   - Continue only after explicit approval or requested revisions.
   - Generate the poster only from the approved outline, not directly from unapproved raw notes.

3. **Template preview and selection**
   - Before final poster production, offer the 3 selected LaTeX preview templates in `assets/latex_templates/` and summarize their style/use case.
   - Ask the user to pick one template or approve an adaptation. Use the selected template as the layout starting point, preserving spaces for images, tables, formulas, and text modules.

## Required outline framework

Use this framework for `experiment_outline.md`:

```markdown
# Experiment Outline

## 1. Confirmed Engineering Snapshot
- Language, size/orientation, output format:
- Project folder and file paths:
- AI interface/API and image generation setup:
- Build/export tools:

## 2. Poster Identity and Assets
- Title and subtitle:
- Authors and affiliations:
- Contact / QR:
- Branding/logo/image-use decisions:

## 3. Scientific Story
- Background:
- Motivation / problem:
- Research goal or hypothesis:
- Key contribution:

## 4. Theory and Formula Panel
- Core theory:
- Key formula(s):
- Symbol definitions:
- Link between theory and measured data:

## 5. Experimental Workflow
- Pipeline steps:
- Mandatory flowchart content:
- Experimental schematic content:
- Inputs, controls, outputs:

## 6. Data and Results
- Datasets and variables:
- Key numeric results:
- Required comparisons:
- Uncertainty/statistics:
- Candidate diverse chart types:

## 7. Interpretation
- Main takeaways:
- Limitations:
- Future work:

## 8. References and Assets
- References:
- Existing images/logos and approved use:
- AI-generated visuals needed:
- Missing information:
```

## Poster content rules

- Keep the title bar concise: title, optional subtitle, authors, affiliations/logos as approved.
- Do not show production details on the poster: no file paths, prompts, API/model names, script names, storage locations, or “AI-generated” process captions.
- Include a workflow/pipeline flowchart unless the user explicitly refuses it. If workflow details are missing, draft conservative placeholder steps for user confirmation before final export.
- Include theory formulas when the topic has mathematical or mechanistic basis.
- Include an experimental schematic when enough information or source imagery exists.
- Use text + image modules rather than long prose blocks.
- Use academic minimalist styling for all generated visuals: clean vector-like design, restrained colors, high contrast, whitespace, clear labels, no clutter, no decorative 3D.

## Layout rules

- Make the poster visually modular in both landscape and portrait formats: prefer multiple modules per row and multiple modules per column, with balanced gutters, aligned edges, and consistent section heights.
- Avoid single long vertical stacks or one oversized text column unless the poster size forces it.
- Avoid large empty regions. If whitespace becomes visually dominant, rebalance modules, enlarge key figures, add callout boxes, use compact summary tables, add formula/definition sidebars, place approved logos/contact blocks, add subtle section backgrounds, or convert one result into a small-multiple panel—without cluttering the design.
- Typical order: title bar; motivation/goal + theory/formulas; workflow flowchart + experimental schematic; diverse results; analysis/future work; references/contact.
- Vary layouts by project: central pipeline with surrounding evidence, result-centered grid, theory-left/results-right, or top methods/bottom results.
- Fit text to space: no overlap, no clipping, concise bullets, readable labels.
- During final QA, inspect the full poster for blank zones. Keep intentional whitespace for readability, but fix accidental large gaps by resizing, moving, or adding scientifically useful modules.

## Visual and data strategy

- Prefer AI-generated visual panels for polished chart layouts, workflow diagrams, experimental schematics, mechanisms, graphical abstracts, and composite result panels.
- Use Python for data cleaning, statistics, exact values, validation plots, and tables that feed AI prompts.
- Never let AI invent or alter quantitative results. Verify all AI-rendered chart labels, values, trends, legends, and units against Python outputs or the approved outline.
- Prioritize chart diversity. When data permits, use at least three distinct forms, such as:
  - Trend/comparison: line, grouped bar, stacked bar, slope chart.
  - Distribution/uncertainty: box, violin, beeswarm, raincloud, CI/error-bar plot.
  - Relationship/model: scatter with regression, calibration, residual, prediction-vs-observation.
  - Matrix/high-dimensional: heatmap, correlation matrix, PCA, UMAP, t-SNE, confusion matrix.
  - Domain-specific: volcano, MA, Manhattan, ROC/PR, Kaplan-Meier, Bland-Altman.
  - Process/spatial: Sankey, network, pathway, map, microscopy grid, segmentation overlay.
  - Compact summary: table with sparklines, mini-bars, effect sizes, highlighted best values.
- If data are too limited for three forms, use the maximum honest variety and avoid redundant chart types.

## AI image script rule

If AI image generation is used, first create `poster_work/scripts/generate_ai_image.py` from `scripts/generate_ai_image_template.py`, adapting it to the user's API documentation and key handling. Reuse that script for all later image generation. Save prompts, parameters, outputs, and metadata under `poster_work/assets/ai_images/`, but keep those details out of the poster.

## Format notes
- LaTeX: use one of the 3 selected preview templates unless the user requests another template; compile PDF when possible.
- PPT/PPTX: create one poster-sized editable slide; export a PDF proof when possible.

## Final response checklist
Report final source/export paths, project subfolder, remaining placeholders, and build/export command if relevant.
