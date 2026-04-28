import requests
from bs4 import BeautifulSoup
import pandas as pd

# The Target Array
final_extraction = []

# Mission: Scrape multiple data points across multiple pages
for page in range(1, 3):  # Let's hit 2 pages for the proof
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        # Data Point 1: Title
        title = book.h3.a['title']
        
        # Data Point 2: Price
        price = book.find('p', class_='price_color').text.replace('Â£', '')
        
        # Data Point 3: Rating (Extracted from the class name!)
        # The class looks like "star-rating Three"
        rating_classes = book.find('p', class_='star-rating')['class']
        rating = rating_classes[1] # This gets the "Three", "Four", etc.
        
        final_extraction.append({
            "Title": title,
            "Price (£)": float(price),
            "Rating": rating
        })

# The Payload Delivery
df = pd.DataFrame(final_extraction)
df.to_csv("Professional_Market_Data.csv", index=False)

print("\n--- EXTRACTED DATASET ---")
print(df.head())
print(f"\nTotal Rows Secured: {len(df)}")