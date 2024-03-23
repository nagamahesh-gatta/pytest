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
    more_button = browser.find_element(By.XPATH,"//span[@class='more-arr']")
    action_inst = ActionChains(browser)
    action_inst.move_to_element(more_button).perform()
    time.sleep(3)
    browser.find_element(By.XPATH,"//span[normalize-space()='Cruise']").click()
    time.sleep(2)
