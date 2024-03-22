import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# text property
@pytest.mark.usefixtures
def test_text_property(browser):

    browser.get("https://www.yatra.com/")
    text = browser.find_element(By.XPATH, "//span[normalize-space()='Popular International Flight Routes']").text
    print(text)

