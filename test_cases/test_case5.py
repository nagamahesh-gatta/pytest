import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# find_elements
@pytest.mark.usefixtures
def test_find_element(browser):

    browser.get("https://www.yatra.com/")
    browser.maximize_window()
    browser.implicitly_wait(10)
    list_of_anchor_tags = browser.find_elements(By.TAG_NAME,'a')
    print(len(list_of_anchor_tags))
    for items in list_of_anchor_tags:
        print(items.text)
    time.sleep(3)
