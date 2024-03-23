import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")


@pytest.fixture
def browser():
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
