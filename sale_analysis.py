
import pandas as pd

# Load the sales data from CSV file
sales_data = pd.read_csv('diwali_sales_data.csv')

# Display the first few rows of the dataset
print("Sample of the sales data:")
print(sales_data.head())

# Calculate total sales
total_sales = (sales_data['Quantity'] * sales_data['Price']).sum()
print("\nTotal sales during Diwali:", total_sales)

# Calculate the most sold item
most_sold_item = sales_data.groupby('Item')['Quantity'].sum().idxmax()
print("\nThe most sold item during Diwali:", most_sold_item)

# Calculate the total revenue per item
revenue_per_item = sales_data.groupby('Item')['Price'].sum().sort_values(ascending=False)
print("\nTotal revenue per item:")
print(revenue_per_item)

# Calculate the average price per item
average_price_per_item = sales_data.groupby('Item')['Price'].mean().sort_values(ascending=False)
print("\nAverage price per item:")
print(average_price_per_item)

# Plotting total revenue per item
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
revenue_per_item.plot(kind='bar', color='skyblue')
plt.title('Total Revenue per Item during Diwali Sales')
plt.xlabel('Item')
plt.ylabel('Revenue')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
