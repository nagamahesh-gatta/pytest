from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(1)
driver.set_window_size(1024, 768)
time.sleep(3)
# Close browser
driver.quit()