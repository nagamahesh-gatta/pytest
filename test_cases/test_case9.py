import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
    browser.find_element(By.XPATH,"//span[normalize-space()='Traveller']").click()


    travellers_hotels = browser.find_element(By.XPATH, "//label[@class='travellerLabel']")
    travellers_hotels.click()
    browser.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
    print(browser.find_element(By.CSS_SELECTOR,".ageselect").is_displayed())
    time.sleep(3)
