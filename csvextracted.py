
# here we will extract the book title and its price using its html code

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

#this gives the chrome a useable driver
driver= webdriver.Chrome()

#this will open the webpage
driver.get("https://books.toscrape.com")

# will show the webpage for 3s (waits for 3s them goes to the next statement)
time.sleep(3)

#developer's switch is added for the output as only title or title and price
switch=0

if(switch==0):

    #this copies a whole chunk of code
    book_elements = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    
    books_data=[]

    for book in book_elements:

        #as we now want two things from the same block of code, we need to use find elements to find both attribute
        #this finds the h3 a block and then gets the title from title attribute
        title = book.find_element(By.CSS_SELECTOR,"h3 a").get_attribute("title")

        #as in the html code of the webpage, the price is written in the class price_color we put that as attribute
        price = book.find_element(By.CLASS_NAME,"price_color").text
        
        # getting the rating 
        rating_class = book.find_element(By.CSS_SELECTOR,"p.star-rating").get_attribute("class").split()
        rating = rating_class[1] if len(rating_class) > 1 else "Not Ranked"

        #here we are making a dict to add into the csv file
        books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

driver.quit()

df = pd.DataFrame(books_data)
df.to_csv("Books.csv", index= False, encoding= "utf- 8" )
print("DONE")