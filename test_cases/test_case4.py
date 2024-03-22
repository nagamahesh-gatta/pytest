import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# find_elements
@pytest.mark.usefixtures
def test_tmc_sign_in(browser):

    browser.get("https://svlnsd.aped-tms-dp-master-temple.pages.dev/en-in/home")
    browser.maximize_window()
    browser.implicitly_wait(10)
    sign_in_or_sign_up_btn = browser.find_element(By.XPATH,"//div[contains(text(),'SIGN IN / SIGN UP')]")
    sign_in_or_sign_up_btn.click()
    mobile_number = browser.find_element(By.XPATH,"//input[@placeholder='Enter Your 10 digit mobile number']")
    mobile_number.send_keys("9052932167")
    time.sleep(3)


