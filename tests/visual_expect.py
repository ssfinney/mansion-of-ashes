from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageChops
from playwright.sync_api import Page


def assert_page_screenshot(
    page: Page,
    *,
    path: str,
    threshold: float = 0.1,
    full_page: bool = True,
    failures_root: Path,
) -> None:
    baseline_path = Path(path)
    baseline_path.parent.mkdir(parents=True, exist_ok=True)

    actual_bytes = page.screenshot(full_page=full_page)
    actual_image = Image.open(__import__("io").BytesIO(actual_bytes)).convert("RGBA")

    update_snapshots = os.getenv("UPDATE_SNAPSHOTS", "").lower() in {"1", "true", "yes"}
    if not baseline_path.exists() or update_snapshots:
        actual_image.save(baseline_path)
        return

    baseline_image = Image.open(baseline_path).convert("RGBA")

    target = failures_root / baseline_path.stem
    target.mkdir(parents=True, exist_ok=True)

    if actual_image.size != baseline_image.size:
        actual_image.save(target / "actual.png")
        baseline_image.save(target / "baseline.png")
        raise AssertionError(
            f"Screenshot size mismatch for {baseline_path.name}: actual={actual_image.size} baseline={baseline_image.size}"
        )

    diff = ImageChops.difference(actual_image, baseline_image)
    bands = diff.split()
    merged = bands[0]
    for band in bands[1:]:
        merged = ImageChops.lighter(merged, band)

    changed_pixels = sum(merged.histogram()[1:])
    total_pixels = actual_image.size[0] * actual_image.size[1]
    ratio = changed_pixels / max(total_pixels, 1)

    if ratio > threshold:
        actual_image.save(target / "actual.png")
        baseline_image.save(target / "baseline.png")
        diff.save(target / "diff.png")
        raise AssertionError(
            f"Visual regression for {baseline_path.name}: {ratio:.4f} > allowed threshold {threshold:.4f}"
        )
