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

    browser.get("https://secure.yatra.com/")
    browser.execute_script("window.scrollTo(0, 300)")
    parent_window = browser.current_window_handle
    print(parent_window)
    browser.find_element(By.XPATH,"//img[@alt='Amazon Pay ICICI Bank Credit Card']").click()
    all_windows = browser.window_handles
    for window in all_windows:

        if window != parent_window:
            browser.switch_to.window(window)
            browser.find_element(By.ID,"BE_flight_origin_city").send_keys("hyder", Keys.ENTER)
            time.sleep(4)
            break

    browser.switch_to.window(parent_window)
    browser.find_element(By.XPATH,"//img[@class='conta iner']")
    time.sleep(4)
