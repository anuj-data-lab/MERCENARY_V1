import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target parameters
target_price = 50.00
mission_active = True
cycle_count = 0

print("--- WATCHTOWER LIVE DEPLOYMENT ---")

try:
    while mission_active:
        cycle_count += 1
        print(f"\n[Cycle {cycle_count}] Initiating Check...")
        
        # We call the function we built in the previous step
        # Note: In a real script, the check_price function code would be here
        def check_price(target_price):
            url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
            headers = {"User-Agent": "Mozilla/5.0"} # Our basic disguise
            

            try:
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

            except requests.exceptions.ConnectionError:
                print("!!! SIGNAL LOST: Network unreachable. Retrying in next cycle... !!!")
                return False
            except Exception as e:
                print(f"Unexpected Breach: {e}")
                return False

        alert_triggered = check_price(target_price)
        
        if alert_triggered:
            print("MISSION ACCOMPLISHED: Target hit. Shutting down to prevent duplicate alerts.")
            mission_active = False
        else:
            print("Cooldown initiated. Waiting 10 seconds for next sweep...")
            time.sleep(10) # The 'Sleep' keeps you from getting banned for spamming

except KeyboardInterrupt:
    print("\nManual Override Detected. Tank returning to base.")