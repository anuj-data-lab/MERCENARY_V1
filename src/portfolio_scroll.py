from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

try:
    print("Mission Start: Targeting Infine Scroll Site...")
    driver.get("https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html")

    # The "Scroll Loop" - simulating a human scrolling down to load data.

    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(3): #scroll three times
        print(f"Scrolling down... Level{i+1}")
        driver.execute_script("window.scrollTo(0, document.bodyScrollHeight);")
        time.sleep(2)

    # capture the final state
    titles = driver.find_elements("css selector", "h3 a")
    print(f"Successfully extracted {len(titles)} titles using Infinite Scroll Logic.")

    for title in titles[:5]:
        print(f"Verfied Asset: {title.get_attribute('title')}")
    
finally:
    driver.quit()
    print("\nExtraction Complete. System Cooling Down")