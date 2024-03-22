from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://imageresizer.com/")

# Find the file upload button and click it
upload_btn = driver.find_element(By.XPATH, "//button[@class='flex items-center py-5 px-6 gap-4 border-r-slate-200 dark:border-r-darkSurface-100 border-r hover:bg-irGray-200 dark:hover:bg-darkSurface-300 rounded-md']")
upload_btn.click()

# Find the file input element and send the file path
file_input = driver.find_element(By.ID, 'upload')
file_path = "/home/nagamaheshgatta/Pictures/Branching.png"
file_input.send_keys(file_path)

# Wait for a few seconds (adjust as needed) for the file to be uploaded
time.sleep(5)

driver.close()
