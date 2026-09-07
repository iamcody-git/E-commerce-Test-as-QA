from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product(driver):

    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # Username
    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    # Password
    wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    ).send_keys("secret_sauce")

    # Login button
    wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()

    # Wait until product page is loaded
    wait.until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )

    # Add Bike Light to cart
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-bike-light")
        )
    ).click()

    # Final assertion
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"