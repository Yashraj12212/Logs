# here we will extract the book title and its price using its html code

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


#this gives the chrome a useable driver
driver = webdriver.Chrome() 

#this will open the webpage
driver.get("https://books.toscrape.com")

# will show the webpage for 3s (waits for 3s them goes to the next statement)
time.sleep(3) 

switch=0 #developer's switch is added for the output as only title or title and price

if(switch==1):

    #finds the <h3> block and copys it as whole in book elements which consists the price and title
    #the ccs selector uses the css pattern ("article.product_pod h3 a")

    book_elements= driver.find_elements(By.CSS_SELECTOR, "article.product_pod h3 a") 
    
    for book in book_elements:
        #saves the book's title into varible title by finding the attribute in the code with same name
        title = book.get_attribute("title")
        print(f"{title}")

else:

    book_elements= driver.find_elements(By.CSS_SELECTOR, "article.product_pod") 
    
    for book in book_elements:
        #as we now want two things from the same block of code, we need to use find elements to fid both attribute
        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        #as in the html code of the webpage, the price is written in the class price_color we put that as attribute
        price = book.find_element(By.CLASS_NAME,"price_color").text

        # getting the rating 
        ratingelement = book.find_element(By.CSS_SELECTOR, "p.star-rating")
        rating_class = ratingelement.get_attribute("class").split() # ['star rating', 'three'] create a list like this
        rating = rating_class[1] if len(rating_class)> 1 else "Not Ranked"
        
        print(f"{title} - {price} - {rating} stars")

driver.quit()