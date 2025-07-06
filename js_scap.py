#this code scapes data from a js site 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()

#this is a js site which is farely easy to scape
driver.get("https://quotes.toscrape.com/js/")

#As Js sites need more time to load we can't just we sleep funtion, we need to load the site first the scape the data
# this funtion loads the site until quote code block is loaded
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"quote"))
)

#find the quote code block
quote_elements = driver.find_elements(By.CLASS_NAME,"quote")

data = []

#loop to dissect the code block and take the imp data out from it
for quote in quote_elements:

    #serches text class element
    text = quote.find_element(By.CLASS_NAME,"text").text
    
    #serches author class element
    author = quote.find_element(By.CLASS_NAME,"author").text

    #for tags, we will first take out a block with class name tag, then loop to take all the tags out singularly
    #tags is the parent class and tag is the class name
    tag_elements = quote.find_elements(By.CSS_SELECTOR, ".tags a tag")
    tags = [tag.text for tag in tag_elements]

    #putting data into dict
    data.append({
        "Quote" : text,
        "Author" : author,
        "Tags" : ", ".join(tags)
        })

driver.quit()

#putting data into csv
df = pd.DataFrame(data)
df.to_csv("quotes_page1.csv", index= False, encoding="utf-8")
print("Done")
