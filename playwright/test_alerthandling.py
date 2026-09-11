from playwright.sync_api import Page, expect

def test_alert(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once("dialog", lambda dialog:dialog.accept())

    page.get_by_text("Click for JS Alert").click()
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")

def test_confirm(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once("dialog", lambda dialog:dialog.dismiss())

    page.get_by_text("Click for JS Confirm").click()
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")
    page.wait_for_timeout(2000)

def test_prompt(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once("dialog", lambda dialog:dialog.accept("playwright demo"))

    page.get_by_text("Click for JS Prompt").click()
    expect(page.locator("#result")).to_have_text("You entered: playwright demo")
    page.wait_for_timeout(2000)