# locate element by id and name

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(2)

#locate user name
# located by id
# username = driver.find_element(By.ID, value="user-name")

# located by name
username = driver.find_element(By.NAME, value="user-name")

password = driver.find_element(By.ID, value="password")

#enter username from website
username.send_keys("standard_user")
time.sleep(2)

#enter password get from website 
password.send_keys("secret_sauce")
time.sleep(5)

driver.quit()