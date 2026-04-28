import requests
from bs4 import BeautifulSoup
import pandas as pd

def check_price(target_price):
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    headers = {"User-Agent": "Mozilla/5.0"} # Our basic disguise
    
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # Extract the price and convert to a float
    price_text = soup.find('p', class_='price_color').text
    # Removing currency symbol (adjusting for the site's unique encoding)
    current_price = float(price_text.replace('£', '').replace('Â', ''))
    
    print(f"Current Market Price: £{current_price}")
    
    if current_price <= target_price:
        print("!!! ALERT: TARGET PRICE MET. INITIATE PURCHASE PROTOCOL. !!!")
        return True
    else:
        print(f"Status: Holding. Price is £{current_price - target_price} above target.")
        return False

# Execute the watchtower
# Let's say our client only wants to buy if the price hits £50.00
check_price(50.00)