# Top-tier CS Pipeline Diagram Prompt

Use for computer science, machine learning, vision, remote sensing, and optimization posters that need a polished conference-paper-style framework figure.

```text
A professional, high-quality computer science academic pipeline diagram for a top-tier conference paper, similar to CVPR/ICCV figure aesthetics.

[Structure and Layout]
Create a clean 16:9 vector-style pipeline diagram divided into three distinct shaded panels:
- Top-left panel: pastel light green background.
- Top-right panel: pastel light blue background.
- Bottom panel: clean white background spanning the width.
Use clear panel boundaries, balanced whitespace, aligned edges, and a technical blueprint-like composition.

[Top-left Panel: Encoder Stack]
Illustrate a neural network encoder stack processing a 3D data cube input labeled {$Y$, HR-MSI} into an output latent block labeled {$Z$}.
Show the 3D cube, stacked encoder layers, vector-style bounding boxes, and solid black flow arrows from input to encoder to output.

[Top-right Panel: Iterative Optimization]
Show an iterative machine learning optimization loop with a large circular arrow.
Include crisp probability symbols such as {$p(X \mid Z,\theta)$}, a covariance matrix icon, and a colorful line graph with overlapping Gaussian curves.
Add dotted red feedback arrows to indicate iterative refinement, without clutter.

[Bottom Panel: Objective Function]
Display the large formula
{$\max_{Z,\theta,\phi}\ \log p(Z \mid X,Y,\phi) + \log p(\theta \mid X,Y)$}
in a sharp LaTeX Computer Modern-style math font.
Add curly horizontal brackets underneath to group the two terms, with concise labels such as "latent reconstruction term" and "parameter prior term".

[Visual Style]
Clean vector graphics, sharp thin lines, minimalist flat design, solid black arrows, dotted red feedback arrows, high contrast, no 3D photorealistic rendering, no glossy shadows, no decorative gradients.
All text and variables should look like crisp LaTeX math typography.
Make the diagram presentation-ready for an academic poster or paper figure.

[Output]
Aspect ratio 16:9. High resolution. White margins. No watermark. No extra explanatory paragraphs outside the diagram.
```

## Adaptation checklist

- Replace variables, model names, likelihood terms, and panel labels with the approved experiment outline.
- Preserve the three-panel structure only when it matches the scientific story; otherwise adapt the panels while keeping the same visual language.
- Keep generated chart shapes illustrative unless exact plotted data are supplied; never let the image model invent quantitative values.
- Save prompts and outputs under `poster_work/assets/ai_images/`, but keep prompt/model/API details out of the final poster.
