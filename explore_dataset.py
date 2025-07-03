import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv("data.csv", encoding='ISO-8859-1')


# Display first 5 rows
print(" First 5 rows:")
print(df.head())

# Dataset shape
print("\nRows and Columns:", df.shape)

# Column names and data types
print("\n Data Types and Non-Null Counts:")
print(df.info())

# Check for missing values
print("\n Missing Values:")
print(df.isnull().sum())

# Check for duplicates
print("\n Duplicate Rows:", df.duplicated().sum())

# Create a new Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Summary statistics
print("\n Summary Statistics:")
print(df.describe(include='all'))
input("\nPress Enter to exit...")
# Drop duplicate rows
df.drop_duplicates(inplace=True)
print("\n Duplicates removed.")
# STEP 3.2 — Handle missing values

# Check missing values
print("\n Missing Values:")
print(df.isnull().sum())

# Drop rows with missing Description or CustomerID
df.dropna(subset=['Description', 'CustomerID'], inplace=True)
print("\n Dropped rows with missing Description or CustomerID.")
# STEP 3.3 — Clean column names (remove spaces)
df.columns = df.columns.str.strip().str.replace(' ', '_')
print("\n Cleaned column names:", df.columns.tolist())
# STEP 3.4 — Convert InvoiceDate column to datetime
if 'InvoiceDate' in df.columns:
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    print("\n  Converted 'InvoiceDate' to datetime format.")
# STEP 3.5 — Final dataset shape
print("\n Final Dataset Shape:", df.shape)
input("\nPress Enter to exit...")
# STEP 4.1 — Add Month column for analysis
df['Month'] = df['InvoiceDate'].dt.to_period('M')
print("\n  Added 'Month' column:", df['Month'].head())
# STEP 4.2 — Monthly Revenue
monthly_revenue = df.groupby('Month')['Revenue'].sum()
print("\n Monthly Revenue:\n", monthly_revenue)
# Pause
input("\nPress Enter to exit...")
# STEP 4.3 — Plot Monthly Revenue
monthly_revenue.plot(kind='line', marker='o', figsize=(10, 5), title='Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.grid(True)
plt.tight_layout()
plt.show()
# STEP 4.4 — Top 5 Products by Revenue
top_products = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(5)
print("\n Top 5 Products by Revenue:\n", top_products)
# STEP 4.5 — Country-wise Revenue
country_revenue = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)
print("\n Revenue by Country:\n", country_revenue.head(10))  # Show top 10 countries
# STEP 5 — Export Cleaned Data
df.to_csv("cleaned_ecommerce_data.csv", index=False)
print("\n Cleaned dataset saved as 'cleaned_ecommerce_data.csv'")
try:
    input("\nScript finished. Press Enter to exit...")
except EOFError:
    pass













