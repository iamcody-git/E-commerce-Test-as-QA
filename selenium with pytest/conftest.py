from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    #setup
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver

    #teardown
    driver.quit()
