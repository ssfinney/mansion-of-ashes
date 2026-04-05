from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageChops


@dataclass
class PageScreenshotExpect:
    page: object
    baseline_dir: Path
    failure_dir: Path
    update_snapshots: bool

    def to_have_screenshot(self, name: str, threshold: float = 0.1) -> None:
        baseline_path = self.baseline_dir / name
        baseline_path.parent.mkdir(parents=True, exist_ok=True)

        shot_bytes = self.page.screenshot(full_page=True)
        actual_img = Image.open(BytesIO(shot_bytes)).convert("RGBA")

        if self.update_snapshots or not baseline_path.exists():
            baseline_path.write_bytes(shot_bytes)
            return

        baseline_img = Image.open(baseline_path).convert("RGBA")

        if actual_img.size != baseline_img.size:
            self._write_failure_artifacts(name, actual_img, baseline_img)
            raise AssertionError(
                f"Screenshot size mismatch for {name}: "
                f"actual={actual_img.size}, baseline={baseline_img.size}"
            )

        diff = ImageChops.difference(actual_img, baseline_img)
        diff_ratio = self._non_matching_ratio(diff)

        if diff_ratio > threshold:
            self._write_failure_artifacts(name, actual_img, baseline_img, diff)
            raise AssertionError(
                f"Visual diff too high for {name}: {diff_ratio:.4f} > {threshold:.4f}"
            )

    def _non_matching_ratio(self, diff: Image.Image) -> float:
        alpha = diff.split()[-1]
        non_zero = sum(1 for px in alpha.getdata() if px != 0)
        return non_zero / (diff.width * diff.height)

    def _write_failure_artifacts(
        self,
        name: str,
        actual: Image.Image,
        baseline: Image.Image,
        diff: Image.Image | None = None,
    ) -> None:
        target = self.failure_dir / Path(name).stem
        target.mkdir(parents=True, exist_ok=True)
        baseline.save(target / "baseline.png")
        actual.save(target / "actual.png")
        if diff is None:
            diff = ImageChops.difference(actual, baseline)
        diff.save(target / "diff.png")



def expect(page: object, baseline_dir: Path, failure_dir: Path, update_snapshots: bool) -> PageScreenshotExpect:
    return PageScreenshotExpect(
        page=page,
        baseline_dir=baseline_dir,
        failure_dir=failure_dir,
        update_snapshots=update_snapshots,
    )
