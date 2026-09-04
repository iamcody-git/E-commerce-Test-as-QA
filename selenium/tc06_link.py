from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Username
# username = driver.find_element(
#     By.XPATH,
#     "//input[@id='user-name']"
# )

# locate Username by tagname
username = driver.find_element(
    By.TAG_NAME,
    value="input"
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
# button = driver.find_element(
#     By.XPATH,
#     "//input[@id='login-button']"
# )

# locate Login by classname
button = driver.find_element(
    By.CLASS_NAME,
    value='btn_action'
)

button.click()

# full link text 
# productlink = driver.find_element(
#     By.LINK_TEXT,
#     value="Sauce Labs Backpack")


# partial link text 
productlink = driver.find_element(
    By.PARTIAL_LINK_TEXT,
    value="Backpack")


time.sleep(2)
productlink.click()

time.sleep(2)
driver.quit()