#!/usr/bin/env python3
"""Make a raster image background transparent.

Usage:
  python make_image_transparent.py input.png output.png
  python make_image_transparent.py input.jpg output.png --background corner --tolerance 28
  python make_image_transparent.py input.png output.png --background "#ffffff" --tolerance 18

The script is intended for poster asset cleanup, such as turning generated
icons, diagrams, or logo-like images into transparent PNG assets before layout.
It does not call external AI services.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_hex_color(value: str) -> tuple[int, int, int]:
    value = value.strip()
    if value.startswith("#"):
        value = value[1:]
    if len(value) != 6:
        raise ValueError("Hex background color must be in #RRGGBB format.")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def estimate_corner_color(image: Image.Image, sample_size: int) -> tuple[int, int, int]:
    rgb = image.convert("RGB")
    width, height = rgb.size
    sample_size = max(1, min(sample_size, width, height))
    boxes = [
        (0, 0, sample_size, sample_size),
        (width - sample_size, 0, width, sample_size),
        (0, height - sample_size, sample_size, height),
        (width - sample_size, height - sample_size, width, height),
    ]
    red = green = blue = count = 0
    for box in boxes:
        for r, g, b in rgb.crop(box).getdata():
            red += r
            green += g
            blue += b
            count += 1
    return red // count, green // count, blue // count


def color_distance_squared(pixel: tuple[int, int, int], background: tuple[int, int, int]) -> int:
    return sum((channel - bg_channel) ** 2 for channel, bg_channel in zip(pixel, background))


def make_transparent(
    input_path: Path,
    output_path: Path,
    background: tuple[int, int, int],
    tolerance: int,
    soft_edge: int,
) -> None:
    image = Image.open(input_path).convert("RGBA")
    tolerance_sq = tolerance * tolerance
    soft_limit = max(tolerance, tolerance + soft_edge)
    soft_limit_sq = soft_limit * soft_limit

    pixels = []
    source_pixels = image.get_flattened_data() if hasattr(image, "get_flattened_data") else image.getdata()
    for red, green, blue, alpha in source_pixels:
        distance_sq = color_distance_squared((red, green, blue), background)
        if distance_sq <= tolerance_sq:
            pixels.append((red, green, blue, 0))
        elif soft_edge > 0 and distance_sq < soft_limit_sq:
            distance = distance_sq**0.5
            fade = (distance - tolerance) / soft_edge
            pixels.append((red, green, blue, int(alpha * max(0.0, min(1.0, fade)))))
        else:
            pixels.append((red, green, blue, alpha))

    image.putdata(pixels)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Make an image background transparent.")
    parser.add_argument("input", help="Input raster image path.")
    parser.add_argument("output", help="Output PNG path.")
    parser.add_argument(
        "--background",
        default="corner",
        help='Background color: "corner", "white", "black", or #RRGGBB. Default: corner.',
    )
    parser.add_argument("--tolerance", type=int, default=24, help="Color tolerance, 0-441. Default: 24.")
    parser.add_argument("--soft-edge", type=int, default=8, help="Feather transparent edge by this color distance.")
    parser.add_argument("--corner-sample", type=int, default=16, help="Corner sample size when background=corner.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    probe_image = Image.open(input_path)

    if args.background == "corner":
        background = estimate_corner_color(probe_image, args.corner_sample)
    elif args.background == "white":
        background = (255, 255, 255)
    elif args.background == "black":
        background = (0, 0, 0)
    else:
        background = parse_hex_color(args.background)

    make_transparent(
        input_path=input_path,
        output_path=output_path,
        background=background,
        tolerance=max(0, args.tolerance),
        soft_edge=max(0, args.soft_edge),
    )


if __name__ == "__main__":
    main()
