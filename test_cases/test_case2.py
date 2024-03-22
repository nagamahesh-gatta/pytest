import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.mark.usefixtures
def test_login_form(browser):
    browser.get('https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmail.google.com%2Fmail&ec=GAlAFw&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S570618018%3A1711069187193683&theme=mn&ddm=0')
    browser.implicitly_wait(5)
    username_input = browser.find_element(By.NAME,'identifier')
    username_input.send_keys("mahesh.gatta@northalley.com")
    next_button = browser.find_element(By.XPATH,"//span[normalize-space()='Next']")
    next_button.click()
    # browser.switch_to.frame(0)
    password_input = browser.find_element(By.XPATH,"//input[@name='Passwd']")
    password_input.send_keys("M@h*$h@1262")
    browser.find_element(By.XPATH," //span[normalize-space()='Next']").click()
    page_title = browser.title
    assert page_title == 'Gmail', "Sign in page title is mismatch check the site once"





