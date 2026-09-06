from selenium.webdriver.common.by import By
import time

def test_product(driver):
    driver.get("https://www.saucedemo.com/")

    #username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    driver.find_element(By.ID,'add-to-cart-sauce-labs-bike-light').click()

    time.sleep(5)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
