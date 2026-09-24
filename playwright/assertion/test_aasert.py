from playwright.sync_api import Page

def test_assertion(page:Page):
    page.goto("https://www.google.com/")
    assert page.title() == 'Google'
    print('Googling')