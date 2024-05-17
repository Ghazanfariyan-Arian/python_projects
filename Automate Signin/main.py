from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Setup WebDriver
s = Service('/Users/arian/Desktop/Python/chromedriver-mac-arm64/chromedriver')  # Update this to your ChromeDriver path
driver = webdriver.Chrome(service=s)

# Open the registration page
driver.get("https://arxfuture.com/MyFirstDeployment/register.html")

# Assuming the input fields have ids 'username', 'password', and 'email'
# Replace these with the actual IDs or modify the locator strategy (e.g., By.NAME)
username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')

# Input data
username.send_keys("arian")
password.send_keys("1234")

# Submitting the form
# Assuming the button has a unique tag; otherwise, you might need to use its ID or class
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

# Optionally, add some delay to see what happens
import time
time.sleep(10)

# Close the browser
driver.quit()
