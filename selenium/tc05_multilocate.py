from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")


# AND method
# name_password = driver.find_element(
#     By.XPATH,
#     "//input[@type='text' and @id='user-name']"
# )
# name_password.send_keys("standard_user")


# OR method
# name_password = driver.find_element(
#     By.XPATH,
#     "//input[@id='user-name' or @name='user-name']"
# )
# name_password.send_keys("standard_user")


# input method
name_password = driver.find_element(
    By.XPATH,
    value="(//input)[1]"
)
name_password.send_keys("standard_user")


time.sleep(5)
driver.quit()