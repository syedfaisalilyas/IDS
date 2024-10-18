import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta
np.random.seed(42)
products = ['Sofa', 'Dining Table', 'Chair', 'Coffee Table', 'Bed', 
            'Bookshelf', 'Desk', 'Wardrobe', 'Nightstand', 'Armchair']
data = {
    'Order ID': np.arange(1, 501),
    'Product': np.random.choice(products, 500),
    'Price': np.random.uniform(50, 2000, 500),
    'Quantity': np.random.randint(1, 11, 500),
    'Purchase Date': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(500)]
}
df = pd.DataFrame(data)
price_quantity_matrix = df[['Price', 'Quantity']].to_numpy()
df['Total Sales'] = np.prod(price_quantity_matrix, axis=1)
sales_above_100 = df[df['Total Sales'] > 100]
quantity_per_product = df.groupby('Product')['Quantity'].sum()
plt.figure(figsize=(8, 5))
plt.scatter(df['Price'], df['Quantity'], alpha=0.6, color='b')
plt.title('Price vs. Quantity Sold')
plt.xlabel('Price ($)')
plt.ylabel('Quantity Sold')
plt.show()
plt.figure(figsize=(8, 5))
plt.hist(df['Total Sales'], bins=20, color='g', alpha=0.7)
plt.title('Distribution of Total Sales')
plt.xlabel('Total Sales ($)')
plt.ylabel('Frequency')
plt.show()

print("First 5 rows of the DataFrame:")
print(df.head())

print("\nSummary Statistics of Total Sales:")
print(df['Total Sales'].describe())

print("\nSales above $100:")
print(sales_above_100)

print("\nTotal Quantity Sold per Product:")
print(quantity_per_product)
