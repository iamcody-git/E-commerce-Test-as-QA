from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://www.saucedemo.com/")

time.sleep(2)

# Find all input fields
input_fields = driver.find_elements(
    By.TAG_NAME,
    "input"
)

print("Number of input fields:", len(input_fields))

# Enter username and password
input_fields[0].send_keys("standard_user")
input_fields[1].send_keys("secret_sauce")

# Click login
input_fields[2].click()

time.sleep(3)

products = driver.find_elements(
    By.XPATH,
    "//div[@data-test='inventory-item-name']"
)

for product in products:
    print(product.text)

time.sleep(2)

driver.quit()