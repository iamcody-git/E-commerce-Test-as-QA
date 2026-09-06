from selenium.webdriver.common.by import By
import time

def test_valid_login(driver):

    # open webiste
    driver.get("https://www.saucedemo.com/")

    #locate username
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    #locate password
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    #locate login button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2)

    # verify test
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"



