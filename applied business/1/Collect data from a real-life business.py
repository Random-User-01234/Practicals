import pandas as pd

data = {
    'Product': ['Mobile', 'Laptop', 'Rice', 'Shirt', 'Mobile'],
    'Category': ['Electronics', 'Electronics', 'Groceries', 'Clothing', 'Electronics'],
    'Sales': [15000, 45000, 3000, 2000, 18000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nTotal Sales =", df['Sales'].sum())

print("\nSales by Category:")
print(df.groupby('Category')['Sales'].sum())

print("\nStatistics:")
print(df['Sales'].describe())