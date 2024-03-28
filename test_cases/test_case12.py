import pytest
from selenium.common import NoAlertPresentException
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# Dropdown
@pytest.mark.usefixtures
def test_auto_suggestions(browser):
    browser.get("https://www.yatra.com/")
    origin_city = browser.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
    origin_city.click()
    try:
        browser.switch_to.alert.dismiss()

    except NoAlertPresentException:
        origin_city.send_keys("New")
        time.sleep(2)
        cities_list = browser.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        time.sleep(2)
        print(len(cities_list))
        for city in cities_list:
            print(city.text)
            # if "New York (JFK)"


