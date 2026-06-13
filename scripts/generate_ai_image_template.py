#!/usr/bin/env python3
"""Reusable AI image generation script template for poster projects.

Copy this file to poster_work/scripts/generate_ai_image.py, then adapt the
payload and response parsing to the API documentation provided by the user.
Keep API keys in environment variables, not in source files.

Usage:
  $env:IMAGE_API_KEY="..."
  python generate_ai_image.py --prompt prompts/workflow.txt --out ../assets/ai_images/workflow.png --config image_api_config.json
"""

from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path

import requests


def load_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_payload(config: dict, prompt: str) -> dict:
    """Edit this function to match the user's image API documentation."""
    return {
        "model": config.get("model", "IMAGE_MODEL_NAME"),
        "prompt": prompt,
        "size": config.get("size", "1536x1024"),
        "quality": config.get("quality", "high"),
        "n": 1,
    }


def extract_image_bytes(response_json: dict) -> bytes:
    """Edit this function to match the API response format."""
    if "data" in response_json and response_json["data"]:
        item = response_json["data"][0]
        if "b64_json" in item:
            return base64.b64decode(item["b64_json"])
        if "url" in item:
            return requests.get(item["url"], timeout=120).content
    if "image_base64" in response_json:
        return base64.b64decode(response_json["image_base64"])
    raise ValueError("Could not find image bytes in API response. Update extract_image_bytes().")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True, help="Prompt text file.")
    parser.add_argument("--out", required=True, help="Output image path.")
    parser.add_argument("--config", required=True, help="API config JSON.")
    args = parser.parse_args()

    config = load_config(Path(args.config))
    prompt = Path(args.prompt).read_text(encoding="utf-8")
    output_path = Path(args.out)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    key_env = config.get("api_key_env", "IMAGE_API_KEY")
    api_key = os.environ.get(key_env)
    if not api_key:
        raise RuntimeError(f"Missing API key environment variable: {key_env}")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    headers.update(config.get("headers", {}))

    response = requests.post(
        config["endpoint"],
        headers=headers,
        json=build_payload(config, prompt),
        timeout=int(config.get("timeout_seconds", 300)),
    )
    response.raise_for_status()
    response_json = response.json()

    output_path.write_bytes(extract_image_bytes(response_json))
    metadata_path = output_path.with_suffix(output_path.suffix + ".metadata.json")
    metadata_path.write_text(json.dumps({
        "prompt": prompt,
        "config_without_key": {k: v for k, v in config.items() if "key" not in k.lower()},
        "response_keys": list(response_json.keys()),
    }, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

