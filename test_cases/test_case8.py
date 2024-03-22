import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# state of the element
@pytest.mark.usefixtures
def test_state_of_elements(browser):

    browser.get("https://training.openspan.com/login")
    browser.maximize_window()
    browser.implicitly_wait(10)
    user_name = browser.find_element(By.ID,"user_name")
    user_name.send_keys('Mahesh')
    print(browser.find_element(By.XPATH, "//input[@id='login_button']").is_enabled())
    user_pass = browser.find_element(By.ID,"user_pass")
    print(browser.find_element(By.XPATH, "//input[@id='login_button']").is_enabled())
    user_pass.send_keys('Test@123')
    print(browser.find_element(By.XPATH, "//input[@id='login_button']").is_enabled())



