# Academic Poster LaTeX Template Sources

Use this reference when the user requests LaTeX output or asks for template choices. Prefer templates with clear licensing and active or well-known usage.

## Recommended template families

| Family | Best for | Notes | Source |
|---|---|---|---|
| Gemini / beamerposter | Modern conference posters with clean columns and strong typography | Built on `beamerposter`; easy to theme for institutions; good default for A0/A1 landscape posters | https://github.com/anishathalye/gemini |
| beamerposter | Familiar Beamer syntax, scalable poster fonts, A0/A1 scientific posters | Combines Beamer with poster-size canvas support; widely used | https://github.com/deselaers/latex-beamerposter |
| tikzposter | Visual block posters with flexible themes | CTAN package for scientific posters using TikZ; useful when visual styling matters | https://ctan.org/pkg/tikzposter |
| baposter | Precise block positioning and compact scientific posters | Good for dense content and controlled box placement; check license of the chosen template | https://github.com/mloesch/baposter |
| Overleaf poster gallery | Fast discovery of size/orientation variants | Use only as inspiration or when license permits; includes A0/A1/A2/A3/A4 and landscape/portrait templates | https://www.overleaf.com/gallery/tagged/poster |

## Bundled preview templates

Offer these 3 selected templates for user selection before final LaTeX poster production:

| File | Style | Best for |
|---|---|---|
| `assets/latex_templates/11_minimal_metric_callouts.tex` | Minimal metric callouts | White-space-heavy portrait posters with oversized standalone quantitative highlights |
| `assets/latex_templates/12_full_width_banner_cards.tex` | Full-width banner cards | Guided engineering/project posters with a dark header and rounded modular cards |
| `assets/latex_templates/13_dense_three_column_conference.tex` | Dense three-column conference | Information-rich landscape posters in a classic conference three-column flow |

## Selection guide

- Choose **Gemini/beamerposter** for most polished academic conference posters.
- Choose **tikzposter** when the poster benefits from large visual blocks, process diagrams, or playful thematic styling.
- Choose **baposter** when the user needs many tightly positioned sections or a legacy scientific poster look.
- Choose an **institution-specific template** only when the user provides branding requirements or the template license permits reuse.

## Implementation notes

- Store copied or adapted template files in `poster_work/assets/templates/`.
- Record source URLs and licenses in `poster_work/README.md`.
- Do not silently copy large third-party templates into the user project if the license is unclear; instead, create a small local template inspired by the structure.
- For Chinese posters, use XeLaTeX or LuaLaTeX and configure CJK fonts explicitly.
