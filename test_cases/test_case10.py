import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# Hidden elements
@pytest.mark.usefixtures
def test_handling_checkboxes(browser):
    browser.get("https://www.sugarcrm.com/au/request-demo/")
    browser.find_element(By.ID,"interest_market_c0").click()
    market_check_box = browser.find_element(By.ID,"interest_market_c0").is_selected()

    time.sleep(2)
