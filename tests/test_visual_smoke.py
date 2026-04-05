from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

import pytest
from playwright.sync_api import Page, expect

ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build"
GAME_PATH = "/mansion-of-ashes.html"
DESKTOP_VIEWPORT = {"width": 1280, "height": 800}
MOBILE_VIEWPORT = {"width": 390, "height": 844}
VISUAL_THRESHOLD = 0.1


@pytest.fixture(scope="session")
def built_game_server() -> str:
    if not (BUILD_DIR / "mansion-of-ashes.html").exists():
        raise FileNotFoundError(
            "Missing build/mansion-of-ashes.html. Run `bash scripts/build-story.sh` before screenshot tests."
        )

    handler = partial(SimpleHTTPRequestHandler, directory=str(BUILD_DIR))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        yield f"http://127.0.0.1:{server.server_port}{GAME_PATH}"
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()


def _open_title(page: Page, game_url: str) -> None:
    page.goto(game_url, wait_until="networkidle")
    expect(page.locator("#passages")).to_contain_text("Mansion of Ashes")


def _click_first_choice_once(page: Page) -> None:
    first_choice = page.locator("#passages a.link-internal").first
    first_choice.click()
    expect(page.locator("#passages")).to_contain_text("You wake under a wool blanket")
    expect(page.locator(".hud")).to_be_visible()


def _go_to_short_final_state(page: Page) -> None:
    # There is no ending reachable in <=3 clicks from Title in the authored passage graph.
    # Capture the shortest stable near-end route: Title -> Bedroom -> Hallway -> Main Exit.
    page.get_by_role("link", name="Begin").click()
    expect(page.locator("#passages")).to_contain_text("You wake under a wool blanket")

    page.get_by_role("link", name="Step into the hallway").click()
    expect(page.get_by_role("link", name="Go to the main exit")).to_be_visible()

    page.get_by_role("link", name="Go to the main exit").click()
    expect(page.locator("#passages")).to_contain_text("front lock is tied into the old electrical release")


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
