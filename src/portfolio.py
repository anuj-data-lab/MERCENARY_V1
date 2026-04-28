import pandas as pd

# Creating a high-value sample dataset
data = {
    'Product Name': ['MacBook Pro M3', 'iPhone 15 Pro', 'Sony WH-1000XM5', 'iPad Air', 'Kindle Paperwhite'],
    'Competitor A Price': [1999, 1099, 348, 599, 139],
    'Competitor B Price': [1949, 1110, 399, 549, 145],
    'Market Average': [1974, 1104.5, 373.5, 574, 142],
    'Status': ['Price Drop', 'Stable', 'Alert: High', 'Price Drop', 'Stable']
}

df = pd.DataFrame(data)

# Save it with professional formatting
filename = "E-commerce_Market_Intelligence_Sample.csv"
df.to_csv(filename, index=False)

print(f"--- ASSET GENERATED: {filename} ---")
print("Open this file. This is what you will attach to your first job proposal.")