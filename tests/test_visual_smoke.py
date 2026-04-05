from __future__ import annotations

import socket
import subprocess
import time
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build"
GAME_PATH = "/mansion-of-ashes.html"
DESKTOP_VIEWPORT = {"width": 1280, "height": 800}
MOBILE_VIEWPORT = {"width": 390, "height": 844}
TRANSITION_WAIT_MS = 500
VISUAL_THRESHOLD = 0.1


def _pick_open_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


@pytest.fixture(scope="session")
def built_game_server() -> str:
    if not (BUILD_DIR / "mansion-of-ashes.html").exists():
        raise FileNotFoundError(
            "Missing build/mansion-of-ashes.html. Run `bash scripts/build-story.sh` before screenshot tests."
        )

    host = "127.0.0.1"
    port = _pick_open_port()
    proc = subprocess.Popen(
        ["python", "-m", "http.server", str(port), "--bind", host, "--directory", str(BUILD_DIR)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    deadline = time.monotonic() + 5
    while time.monotonic() < deadline and proc.poll() is None:
        try:
            with socket.create_connection((host, port), timeout=0.2):
                break
        except OSError:
            time.sleep(0.1)
    else:
        raise RuntimeError("Failed to start local HTTP server for screenshot tests")

    try:
        yield f"http://{host}:{port}{GAME_PATH}"
    finally:
        proc.terminate()
        proc.wait(timeout=5)


def _open_title(page: Page, game_url: str) -> None:
    page.goto(game_url, wait_until="networkidle")
    expect(page.locator("#passages")).to_contain_text("Mansion of Ashes")
    page.wait_for_timeout(TRANSITION_WAIT_MS)


def _click_first_choice_once(page: Page) -> None:
    first_choice = page.locator("#passages a.link-internal").first
    first_choice.click()
    expect(page.locator(".hud")).to_be_visible()
    page.wait_for_timeout(TRANSITION_WAIT_MS)


def _go_to_short_final_state(page: Page) -> None:
    # There is no ending reachable in <=3 clicks from Title in the authored passage graph.
    # Capture the shortest stable near-end route: Title -> Bedroom -> Hallway -> Main Exit.
    _click_first_choice_once(page)
    page.get_by_role("link", name="Go to the main exit").click()
    expect(page.locator("#passages")).to_contain_text("front lock is tied into the old electrical release")
    page.wait_for_timeout(TRANSITION_WAIT_MS)


def _assert_visual(page: Page, name: str) -> None:
    expect(page).to_have_screenshot(
        f"baseline/{name}.png",
        full_page=True,
        threshold=VISUAL_THRESHOLD,
    )


def test_title_desktop(page: Page, built_game_server: str) -> None:
    page.set_viewport_size(DESKTOP_VIEWPORT)
    _open_title(page, built_game_server)
    _assert_visual(page, "title.desktop")


def test_title_mobile(page: Page, built_game_server: str) -> None:
    page.set_viewport_size(MOBILE_VIEWPORT)
    _open_title(page, built_game_server)
    _assert_visual(page, "title.mobile")


def test_hud_desktop(page: Page, built_game_server: str) -> None:
    page.set_viewport_size(DESKTOP_VIEWPORT)
    _open_title(page, built_game_server)
    _click_first_choice_once(page)
    _assert_visual(page, "hud.desktop")


def test_hud_mobile(page: Page, built_game_server: str) -> None:
    page.set_viewport_size(MOBILE_VIEWPORT)
    _open_title(page, built_game_server)
    _click_first_choice_once(page)
    _assert_visual(page, "hud.mobile")


def test_ending_desktop(page: Page, built_game_server: str) -> None:
    page.set_viewport_size(DESKTOP_VIEWPORT)
    _open_title(page, built_game_server)
    _go_to_short_final_state(page)
    _assert_visual(page, "ending.desktop")
