from playwright.sync_api import Page, Expect

def test_has_title(page:Page):
    page.goto("https://www.saucedemo.com/")

    #usrname
    page.get_by_placeholder("Username").fill("standard_user")

    #password
    page.get_by_placeholder("Password").fill("secret_sauce")

    #login button
    # page.get_by_role("button", name="Login").click()

    # xpath login button
    page.locator("//input[@id='login-button']").click()

    #drop down and change the values 
    dd = page.get_by_role("combobox", name="Sort products")
    dd.select_option("lohi")
    page.wait_for_timeout(5000)
    dd.select_option("za")


    page.wait_for_timeout(5000)
