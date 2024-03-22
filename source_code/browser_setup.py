from selenium import webdriver

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open a website
driver.get('https://www.google.com')

# Close the browser
driver.quit()
