from playwright.async_api import Page, expect

def test_handletabes(page:Page):
    page.goto("https://practice-automation.com/window-operations/")

    with page.expect_popup() as new_tab_info:
        page.click("text=New Tab")

    new_tab = new_tab_info.value
    new_tab.wait_for_load_state()

    print(new_tab.url)
    assert "automatenow" in new_tab.url