from playwright.sync_api import Page, expect

def test_has_title(page:Page):
    page.goto("https://www.saucedemo.com/")

    #username
    page.get_by_placeholder("Username").fill("standard_user")
    #password
    page.get_by_placeholder("Password").fill("secret_sauce")
    #login button
    page.get_by_role("button", name="Login").click()

    # add to cart
    page.locator("#add-to-cart-sauce-labs-backpack").click()

    # shopping cart
    page.locator("#shopping_cart_container").click()

     # shopping cart
    page.locator("#checkout").click()

    #first name
    page.get_by_placeholder("First Name").fill("cody")

    #last name
    page.get_by_placeholder("Last Name").fill("chhetri")

    #zip/postal name
    page.get_by_placeholder("Zip/Postal Code").fill("69582")

    #continue
    page.locator("#continue").click()

    # finish button
    page.locator("#finish").click()

    # burger icon
    page.locator("#react-burger-menu-btn").click()

    #logout
    page.locator("#logout_sidebar_link").click()

   

    page.wait_for_timeout(5000)
