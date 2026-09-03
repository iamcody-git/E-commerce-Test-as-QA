# this script is used to naviagtion automation

from selenium import webdriver
import time

driver = webdriver.Firefox()

#navigate to google
driver.get("https://www.google.com")

time.sleep(5) # used ti delay for 5 sec

# open url of youtube
driver.get("https://www.youtube.com")
time.sleep(5)

# used to go back to google
driver.back()
# used to go forward to youtube

time.sleep(5)
driver.forward()
#used to refresh yt page

time.sleep(5)
driver.refresh()

time.sleep(5)

# used to close the window
driver.quit()
 
