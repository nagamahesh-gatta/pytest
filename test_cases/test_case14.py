import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# Date Selection
@pytest.mark.usefixtures
def test_date_picker(browser):
    browser.get("https://secure.yatra.com/social/common/yatra/signin.htm")
    continue_btn = browser.find_element(By.XPATH,"//button[@id='login-continue-btn']")
    continue_btn.screenshot(".\\test.png")
    continue_btn.click()
    time.sleep(2)
    browser.get_screenshot_as_file("C:\\Users\\Mahesh\\Pictures\\Screenshots\\error.png")
    browser.save_screenshot(".\\test1.png")
