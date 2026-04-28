from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless=new") 
driver = webdriver.Chrome(options=chrome_options)

try:
    print("Infiltrating Target...")
    driver.get("https://books.toscrape.com/")

    # TACTICAL WAIT: Wait for the first book title to be clickable
    # This prevents 'ElementNotInteractableException'
    wait = WebDriverWait(driver, 10)
    first_book = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3 a")))
    
    print(f"Path Clear. Target identified: {first_book.text}")
    
    # Simulate a click to ensure we can navigate
    first_book.click()
    print(f"New Intel: {driver.current_url}")

finally:
    driver.quit()
    print("Exfiltration Successful.")