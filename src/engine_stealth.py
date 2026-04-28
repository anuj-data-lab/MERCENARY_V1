from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")

# THE STEALTH PATCH: Removing the "Bot" markers
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=chrome_options)

# Execute a script to "lie" about being a bot
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

try:
    driver.get("https://www.google.com")
    print(f"Ghost Protocol Active. Current Target: {driver.title}")
    # If this prints without error, you are officially a 'Ghost'
finally:
    driver.quit()