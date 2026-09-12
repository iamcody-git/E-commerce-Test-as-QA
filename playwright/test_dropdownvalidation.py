from playwright.sync_api import Page, expect

def test_dropdown(page: Page):

    page.goto("https://automationtesting.co.uk/dropdown.html")


# dropdown single select
    # dropdown = page.locator("#cars")
    # dropdown.select_option(label="Audi") # select_option is only use if the tag is select otherwise use click
    # page.wait_for_timeout(3000)
    # expect(dropdown).to_have_value("audi")

#radio button
    one = page.get_by_label("One")
    two = page.get_by_label("Two")
    three = page.get_by_label("Three")

    # Select One
    page.get_by_text("One", exact=True).click()
    expect(one).to_be_checked()
    page.wait_for_timeout(3000)

    # Select Two
    page.get_by_text("Two", exact=True).click()
    expect(two).to_be_checked()
    expect(one).not_to_be_checked()
    page.wait_for_timeout(3000)

    # Select Three
    page.get_by_text("Three", exact=True).click()
    expect(three).to_be_checked()
    expect(two).not_to_be_checked()
    page.wait_for_timeout(3000)