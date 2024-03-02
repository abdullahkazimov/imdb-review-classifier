from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def find_reviews(url):
    url += "reviews"
    driver = webdriver.Chrome()
    
    driver.get(url)
    
    driver.implicitly_wait(10)  
    
    reviews = driver.find_elements(By.CLASS_NAME, "text.show-more__control")
    reviews = [review.text for review in reviews]
    
    driver.quit()
    
    
    return reviews

def save_csv(reviews, sentiments):
    df = pd.DataFrame(
        {
            "review":reviews,
            "sentiment":sentiments
        }
    )
    df.to_csv('results.csv')