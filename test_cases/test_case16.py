import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")


# Date Selection
@pytest.mark.usefixtures
def test_date_picker(browser):

    browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
    browser.switch_to.frame(browser.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
    browser.switch_to.frame(0)
    browser.find_element(By.XPATH,"//div[@id='tnb-google-search-mobile-show']//*[name()='svg']").click()
    time.sleep(4)
    browser.switch_to.default_content()
    browser.find_element(By.XPATH,"//button[@id='runbtn']").click()
    time.sleep(3)


