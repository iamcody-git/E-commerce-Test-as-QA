from playwright.sync_api import Page, expect


USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def test_swagscreencast(page:Page):
    page.set_viewport_size({
        'width':1280,
        'height':720
    })

    page.goto("https://www.saucedemo.com/")

    page.screencast.start(
        path="swags.webm"
    )

    page.screencast.show_actions(
        duration=2000,
        font_size=16,
        position='top-right'
    )

    page.screencast.show_chapter(
        title="Swags screencast demo",
        description="This is swags screencast",
        duration=2000
    )

    username = page.get_by_label("Username")
    username.click()
    username.fill(USERNAME)

    password= page.get_by_label("Password")
    password.click()
    password.fill(PASSWORD)

    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.screencast.stop()