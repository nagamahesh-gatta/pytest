import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures
def test_assertions(browser):
    browser.get("http://www.python.org")
    assert "Python" in browser.title
    elem = browser.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("asfdf")
    elem.send_keys(Keys.RETURN)
    assert "No results Found." not in browser.page_source
