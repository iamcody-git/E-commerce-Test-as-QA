
# about xpath absolue and relative path

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(2)

#locating username by relative xpath
username = driver.find_element(By.XPATH, value="//input[@id='user-name']")
password = driver.find_element(By.XPATH, value="//input[@name='password']")

username.send_keys("standard_user")
time.sleep(2)
#enter password get from website 
password.send_keys("secret_sauce")
time.sleep(5)

button = driver.find_element(By.XPATH,value="//input[@id='login-button']")

time.sleep(5)
button.click()

time.sleep(5)
driver.quit()