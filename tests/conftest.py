import os
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GAME_URL = "http://127.0.0.1:8000/build/mansion-of-ashes.html"



def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--update-snapshots",
        action="store_true",
        default=False,
        help="Update visual baseline screenshots.",
    )
    parser.addoption(
        "--run-screenshot-tests",
        action="store_true",
        default=False,
        help="Run Playwright screenshot smoke tests.",
    )



def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    if config.getoption("--run-screenshot-tests"):
        return

    skip_screenshot = pytest.mark.skip(reason="use --run-screenshot-tests to run visual smoke tests")
    for item in items:
        if "screenshot" in item.keywords:
            item.add_marker(skip_screenshot)


@pytest.fixture(scope="session")
def game_url() -> str:
    return os.getenv("SCREENSHOT_GAME_URL", DEFAULT_GAME_URL)


@pytest.fixture(scope="session")
def baseline_dir() -> Path:
    return ROOT / "tests" / "screenshots" / "baseline"


@pytest.fixture(scope="session")
def failure_dir() -> Path:
    path = ROOT / "tests" / "screenshots" / "failures"
    path.mkdir(parents=True, exist_ok=True)
    return path


@pytest.fixture(scope="session")
def update_snapshots(pytestconfig: pytest.Config) -> bool:
    return bool(pytestconfig.getoption("--update-snapshots"))
