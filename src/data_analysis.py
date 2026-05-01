# Import necessary modules
from pathlib import Path  # For handling file paths in a cross-platform way

import pandas as pd  # Pandas library for data manipulation and analysis

# Construct the path to the CSV data file
# __file__ gives the path to this script file
# .resolve() gets the absolute path
# .parent.parent goes up two directories (from src/ to project root)
# Then append 'data' and 'sales_data.csv'
csv_path = Path(__file__).resolve().parent.parent / 'data' / 'sales_data.csv'

# Load the CSV file into a pandas DataFrame
# parse_dates=['Date'] automatically converts the 'Date' column to datetime objects
df = pd.read_csv(csv_path, parse_dates=['Date'])

# Print the total number of rows in the dataset
print('Data rows:', len(df))

# Print a header for the summary statistics section
print('\nSummary statistics for sales and quantity:')

# Generate descriptive statistics for 'Sales' and 'Quantity' columns
# .describe() provides count, mean, std, min, 25%, 50%, 75%, max
print(df[['Sales', 'Quantity']].describe())

# Print a header for the top products section
print('\nTop 5 products by total sales:')

# Group the data by 'Product' and sum the 'Sales' for each group
# Then sort the sums in descending order and take the top 5
print(df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head())

# Print a header for the sales by region section
print('\nSales by region:')

# Group the data by 'Region' and sum the 'Sales' for each region
print(df.groupby('Region')['Sales'].sum())

# Print a header for the monthly sales trend section
print('\nMonthly sales trend:')

# Set 'Date' as the index for time-based operations
# Resample the data by month-end ('ME') and sum the 'Sales' for each month
# Take the first 12 months (head(12))
print(df.set_index('Date').resample('ME')['Sales'].sum().head(12))
