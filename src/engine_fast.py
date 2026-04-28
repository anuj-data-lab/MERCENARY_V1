import requests
from bs4 import BeautifulSoup
import pandas as pd

print("--- Initiating Deep Extraction Protocol ---")
data = []
for page in range(1, 6):
 
    # 1. grab the website
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    # 2. Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')


    # Find all book container
    books = soup.find_all('article', class_='product_pod')

    # loop through each book and pull the title and price
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        data.append({"Title": title, "Price": price})


# 3. Convert to a DataFrame and save

df = pd.DataFrame(data)
df.to_csv("book_prices.csv", index=False)

print("___Extraction Complete___")
print(df.head()) # show the first few rows

# The Cleaning Operation
# Remove the weird symbols and convert the price to a float (a decimal number)
df['Price'] = df['Price'].str.replace('Â£', '').astype(float)

# Now, let's calculate a real metric: The total value of these books
total_value = df['Price'].sum()

print("\n--- Cleaning Complete ---")
print(df.head())
print(f"\nTotal value of books on page: £{total_value:.2f}")

import matplotlib.pyplot as plt

# set up the visual sytle
plt.style.use('ggplot')

# create the histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=5, color='skyblue', edgecolor="black")

# label the mission
plt.title('Market Analysis: Book Price Distribution',  fontsize=15)
plt.xlabel("Price (£)", fontsize=12)
plt.ylabel("Number of Books", fontsize=12)

# save the insights
plt.savefig('price_analysis.png')
print("\n---Visual Intelligence Generated : price analysis.png---")
plt.show()