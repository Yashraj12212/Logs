#this just opens the web page and closes it

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome() #S1-launches chrome 

driver.get("https://books.toscrape.com") #S2- go the books

time.sleep(3) 

print("Page title:", driver.title) # prints page title to confirm

driver.quit()