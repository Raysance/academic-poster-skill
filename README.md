# academic-poster skill

Create academic research posters from experiment outlines, data, author metadata, existing images/logos, and output constraints.

Key behavior:

- Uses two approval gates: first engineering requirements in `project_requirements.md`, then all poster content in `experiment_outline.md`.
- Generates the final poster only from the approved outline.
- Requires a workflow/pipeline flowchart unless the user explicitly refuses it.
- Bundles 3 selected LaTeX preview templates for selection before final poster production.
- Emphasizes theory formulas, experimental schematics, diverse data visualizations, and academic minimalist visuals.
- Keeps production details such as prompts, model names, API details, scripts, and file paths out of the poster itself.

Install by copying the `academic-poster/` folder into any Codex skills directory, for example:

```text
<codex-skills-dir>/academic-poster
```

Included files:

- `SKILL.md` — concise workflow and poster rules.
- `references/latex_templates.md` — LaTeX poster template sources.
- `assets/latex_templates/` — starter LaTeX templates.
- `assets/latex_template_previews/` — compiled PDF/PNG previews and a contact sheet for the 3 selected templates.
- `scripts/generate_data_figures.py` — Python data summary and validation helper.
- `scripts/generate_ai_image_template.py` — adaptable AI image API script template.
