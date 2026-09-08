from selenium.webdriver.common.by import By
import time
from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://www.saucedemo.com/")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()


    # verify test
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    time.sleep(2)



