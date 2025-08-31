import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.jordanbpeterson.com/books/")

while True:
    try:
        load_more = driver.find_element(By.XPATH, '//a[@role="button" and (normalize-space(text())="Load More" or .//span[normalize-space(text())="Load More"])]')
        driver.execute_script("arguments[0].click();", load_more)
        time.sleep(3)  # give time for new content to load
    except Exception as e:
        print("No more 'Load More' button found.")
        print(e)
        break
        
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()
    
book_list = soup.find("div", attrs={"data-id":"e0496e2"})

amazon_links = []
for i in book_list.find_all("a"):
    amazon_links.append(i["href"])

book_info = []


def safe_text(el, default="Not found"):
    """Safely extract text from an element"""
    try:
        return el.text.strip()
    except:
        return default

def find_pages(soup):
    try:
        return soup.find(class_="a-carousel-viewport") \
                   .find("span", string=lambda text: text and "pages" in text).text.strip()
    except:
        return "Not found"

driver = webdriver.Firefox()
for i in amazon_links:
    try:
        driver.get(i)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        book_data ={
             "title": safe_text(soup.find(id="productTitle")),
             "author": safe_text(soup.find(class_="author notFaded").find("a")),
             "pages": find_pages(soup),
             "imageLink": soup.find("img", id="landingImage").get("src")}
        book_info.append(book_data)
        time.sleep(2)
    except Exception as e:
        print("failed to get data from: " + i)
        print(e)
    
driver.quit()

md = "| Title | Author | Pages | Image | Read |\n"
md += "|-------|--------|-------|-------|------|\n"

for b in book_info:
    md += f'| {b["title"]} | {b["author"]} | {b["pages"]} | ![]({b["imageLink"]}) | <input type="checkbox" unchecked/> |\n'

# with open("books.md", "w", encoding="utf-8") as f:
#     f.write(md_table)

with open("books.md", "w", encoding="utf-8") as f:
    f.write(md)
















