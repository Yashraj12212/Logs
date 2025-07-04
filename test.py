from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Optionally define the ChromeDriver service (only needed if not in PATH)
# service = Service("C:/WebDrivers/chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# Simple test using ChromeDriver from PATH
driver = webdriver.Chrome()

# Go to Google
driver.get("https://www.google.com")

# Wait for 3 seconds so you can see it
time.sleep(3)

# Print the page title
print("Page title is:", driver.title)

# Close the browser
driver.quit()