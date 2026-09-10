import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/docs/intro")
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("link", name="Python").click()
    page.get_by_role("link", name="Setting up CI").click()
