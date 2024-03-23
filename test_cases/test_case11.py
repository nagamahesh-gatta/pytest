import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# Dropdown
@pytest.mark.usefixtures
def test_drop_down(browser):
    browser.get("https://www.wikipedia.org/")

    language_dropdown = browser.find_element(By.XPATH,"//select[@id='searchLanguage']")
    select_lang = Select(language_dropdown)
    select_lang.select_by_index(0)
    time.sleep(2)

    # select_lang.select_by_visible_text('hi')
    # time.sleep(2)

    select_lang.select_by_value('en')
    time.sleep(2)


