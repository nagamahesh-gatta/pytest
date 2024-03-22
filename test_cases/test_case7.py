import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# get attribute
@pytest.mark.usefixtures
def test_get_attribute(browser):

    browser.get("https://www.yatra.com/")
    browser.maximize_window()
    browser.implicitly_wait(10)
    get_attribute_using_element = browser.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']")
    value = get_attribute_using_element.get_attribute('value')
    get_attribute_using_element.click()
    print(value)
    time.sleep(3)
