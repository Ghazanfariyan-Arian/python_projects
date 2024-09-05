from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Setup WebDriver
s = Service('/Users/arian/Documents/GitHub/python_projects/UIT_AutoLogin/chromedriver-mac-arm64/chromedriver')  # Update this to your ChromeDriver path
driver = webdriver.Chrome(service=s)
# Open the registration page
driver.get("https://yorku.ca/csstaff/")
# Assuming the input fields have ids 'username', 'password', and 'email'
# Replace these with the actual IDs or modify the locator strategy (e.g., By.NAME)
username = driver.find_element(By.ID, 'mli')
password = driver.find_element(By.ID, 'password')
# Input data
username.send_keys("")
password.send_keys("")
# Submitting the form
# Assuming the button has a unique tag; otherwise, you might need to use its ID or class
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()


input("Press Enter to close the browser...")

