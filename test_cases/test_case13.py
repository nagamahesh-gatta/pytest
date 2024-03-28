import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# Date Selection
@pytest.mark.usefixtures
def test_date_picker(browser):
    browser.get("https://www.yatra.com/")
    origin_date = browser.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
    origin_date.click()
    time.sleep(4)
    all_dates = browser.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td")
    print(len(all_dates))
    for date in all_dates:
        if date.get_attribute("data-date") == "30/03/2024":
            print(date)
            date.click()
            time.sleep(4)
            break
