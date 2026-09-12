from playwright.sync_api import Page

def test_iframe(page: Page):
    page.goto("https://the-internet.herokuapp.com/iframe")

    # Locate the iframe
    frame = page.frame_locator("#mce_0_ifr")

    # Find the editor inside the iframe
    editor = frame.locator("body")

    # Clear existing text
    editor.click()
    editor.press("Control+A")
    editor.fill("Hello from Playwright!")

    # Verify
    print(editor.inner_text())