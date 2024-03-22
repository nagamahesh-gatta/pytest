import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Hidden elements
@pytest.mark.usefixtures
def test_hidden_elements(browser):
    browser.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
    div_content = browser.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
    print(div_content)
    browser.find_element(By.XPATH, "//button[@class='ws-btn w3-hover-black w3-dark-grey']").click()
    div_content = browser.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
    print(div_content)


@pytest.mark.usefixtures
def test_destroy_element(browser):
    browser.get("https://www.yatra.com/")
    browser.find_element(By.XPATH,"//a[@id='booking_engine_hotels']").click()

