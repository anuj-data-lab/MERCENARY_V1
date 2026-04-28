from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 1. setup chrome to run in th(e background(headless)
chrome_options = Options()
chrome_options.add_argument("--headless=new") # to make browisng headless

# 2. initialize the driver
driver = webdriver.Chrome(options=chrome_options)

try:
    print("Launching the Tank...")
    driver.get("https://books.toscrape.com")

# 3. prove it worked

    print(f"Target Acquired: {driver.title}")
    driver.save_screenshot("tank_test.png")
    print("Intelligence captured: tank_test.png saved")

finally:
    driver.quit()
    print("Mission Complete. Driver Offline.")