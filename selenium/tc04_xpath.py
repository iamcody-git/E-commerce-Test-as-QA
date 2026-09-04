from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Username
username = driver.find_element(
    By.XPATH,
    "//input[@id='user-name']"
)

# Password
password = driver.find_element(
    By.XPATH,
    "//input[@name='password']"
)

# Enter login details
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# Login
button = driver.find_element(
    By.XPATH,
    "//input[@id='login-button']"
)

button.click()
time.sleep(3)

# Click Fleece Jacket
product = driver.find_element(
    By.XPATH,
    "//div[text()='Sauce Labs Fleece Jacket']"
)

product.click()
time.sleep(2)

# Add Fleece Jacket to cart
addcart = driver.find_element(
    By.XPATH,
    "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
)

addcart.click()
time.sleep(2)

# Remove Fleece Jacket
remove = driver.find_element(
    By.XPATH,
    "//button[@id='remove-sauce-labs-fleece-jacket']"
)

remove.click()
time.sleep(2)

driver.quit()