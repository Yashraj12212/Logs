# We will try to switch through pages and scape data 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/js/")

data = []

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"quote"))
)

quote_elements = driver.find_elements(By.CLASS_NAME,"quote")

for quote in quote_elements:

    text = quote.find_element(By.CLASS_NAME,"text").text
    author = quote.find_element(By.CLASS_NAME,"author").text
    
    tag_elements = quote.find_elements(By.CSS_SELECTOR, ".tags a tag")
    tags= [tag.text for tag in tag_elements]

    data.append({
        "Quote" : text,
        "Author" : author,
        "Tags" : ", ".join(tags)
    })

#till here, the just extracts the first page's data and saves it in the dict
# Now to load more page, we will make a loop which will run until there is no next button

while True:
    
    # the try tries to find the next if it exists it runs further, if not the while loop ends
    try:
        next_button = driver.find_element(By.CLASS_NAME,"next")
    except:
        break
    
    # this code runs when next button is present, first we extract the link and then click the link
    link = next_button.find_element(By.TAG_NAME,"a")
    link.click()

    #this funtion waits till the page is loaded
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"quote"))
    )

    #after this we repeat the same extraction process as we did for the first page and save it into dict
    quote_elements = driver.find_elements(By.CLASS_NAME,"quote")

    for quote in quote_elements:

        text = quote.find_element(By.CLASS_NAME,"text").text
        author = quote.find_element(By.CLASS_NAME,"author").text
        
        tag_elements = quote.find_elements(By.CSS_SELECTOR, ".tags a tag")
        tags= [tag.text for tag in tag_elements]

        data.append({
            "Quote" : text,
            "Author" : author,
            "Tags" : ", ".join(tags)
        })

#when there is no next page to go on, we will come here and driver will quit
driver.quit()

#saving everything to csv file 
df = pd.DataFrame(data)
df.to_csv("quoteswithpages.csv", index= False, encoding= "utf-8")
print("Done")