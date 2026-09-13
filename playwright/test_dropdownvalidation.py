from playwright.sync_api import Page, expect

def test_dropdown(page: Page):

    page.goto("https://automationtesting.co.uk/dropdown.html")


# dropdown single select
    # dropdown = page.locator("#cars")
    # dropdown.select_option(label="Audi") # select_option is only use if the tag is select otherwise use click
    # page.wait_for_timeout(3000)
    # expect(dropdown).to_have_value("audi")

#radio button
    # one = page.get_by_label("One")
    # two = page.get_by_label("Two")
    # three = page.get_by_label("Three")

    # # Select One
    # page.get_by_text("One", exact=True).click()
    # expect(one).to_be_checked()
    # page.wait_for_timeout(3000)

    # # Select Two
    # page.get_by_text("Two", exact=True).click()
    # expect(two).to_be_checked()
    # expect(one).not_to_be_checked()
    # page.wait_for_timeout(3000)

    # # Select Three
    # page.get_by_text("Three", exact=True).click()
    # expect(three).to_be_checked()
    # expect(two).not_to_be_checked()
    # page.wait_for_timeout(3000)

# checkbox button
    red = page.get_by_label("Red")
    green = page.get_by_label("Green")
    blue = page.get_by_label("blue")

    # Red is initially checked on this website
    expect(red).to_be_checked()

    # Select Green by clicking its visible label
    page.get_by_text("Green", exact=True).click()
    expect(green).to_be_checked()

    # Select blue by clicking its visible label
    page.get_by_text("Blue", exact=True).click()
    expect(blue).to_be_checked()

    # Uncheck Red by clicking its visible label
    page.get_by_text("Red", exact=True).click()
    expect(red).not_to_be_checked()
    page.wait_for_timeout(2000)



    
