#!/usr/bin/env python3
"""Generate poster-ready data figures from CSV files.

Usage:
  python generate_data_figures.py --spec figure_spec.json --out ../assets/figures

Spec example:
{
  "figures": [
    {
      "kind": "line",
      "csv": "../inputs/data/results.csv",
      "x": "time",
      "y": "response",
      "group": "condition",
      "title": "Response over time",
      "xlabel": "Time (s)",
      "ylabel": "Response (a.u.)",
      "filename": "response_time"
    }
  ]
}
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def apply_style() -> None:
    sns.set_theme(context="poster", style="whitegrid")
    plt.rcParams.update({
        "figure.dpi": 180,
        "savefig.dpi": 300,
        "font.size": 18,
        "axes.titlesize": 24,
        "axes.labelsize": 20,
        "legend.fontsize": 16,
    })


def draw_figure(item: dict, output_dir: Path) -> None:
    data = pd.read_csv(item["csv"])
    kind = item.get("kind", "scatter")
    x = item["x"]
    y = item["y"]
    group = item.get("group")

    width = float(item.get("width", 10))
    height = float(item.get("height", 7))
    fig, ax = plt.subplots(figsize=(width, height))

    if kind == "line":
        sns.lineplot(data=data, x=x, y=y, hue=group, marker="o", ax=ax)
    elif kind == "bar":
        sns.barplot(data=data, x=x, y=y, hue=group, errorbar="sd", ax=ax)
    elif kind == "box":
        sns.boxplot(data=data, x=x, y=y, hue=group, ax=ax)
    elif kind == "heatmap":
        pivot = data.pivot(index=item["index"], columns=item["columns"], values=item["values"])
        sns.heatmap(pivot, cmap=item.get("cmap", "viridis"), ax=ax)
    else:
        sns.scatterplot(data=data, x=x, y=y, hue=group, s=120, ax=ax)

    ax.set_title(item.get("title", ""))
    ax.set_xlabel(item.get("xlabel", x))
    ax.set_ylabel(item.get("ylabel", y))
    ax.tick_params(axis="x", labelrotation=item.get("x_rotation", 0))
    fig.tight_layout()

    filename = item.get("filename", f"{kind}_{x}_{y}")
    for extension in item.get("formats", ["png", "svg"]):
        fig.savefig(output_dir / f"{filename}.{extension}", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True, help="Path to figure spec JSON.")
    parser.add_argument("--out", required=True, help="Output directory for figures.")
    args = parser.parse_args()

    spec_path = Path(args.spec)
    output_dir = Path(args.out)
    output_dir.mkdir(parents=True, exist_ok=True)

    apply_style()
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    for item in spec["figures"]:
        draw_figure(item, output_dir)


if __name__ == "__main__":
    main()

