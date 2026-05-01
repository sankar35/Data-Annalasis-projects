# Import necessary modules
from pathlib import Path  # For handling file paths in a cross-platform way

import pandas as pd  # Pandas for data manipulation and reading CSV files
import sqlite3  # SQLite database module for in-memory database operations

# Construct the path to the CSV data file
# __file__ gives the path to this script file
# .resolve() gets the absolute path
# .parent.parent goes up two directories (from src/ to project root)
# Then append 'data' and 'sales_data.csv'
csv_path = Path(__file__).resolve().parent.parent / 'data' / 'sales_data.csv'

# Load the CSV file into a pandas DataFrame
# No parse_dates here since SQLite will handle date strings
df = pd.read_csv(csv_path)

# Create an in-memory SQLite database connection
# ':memory:' means the database exists only in RAM and is temporary
conn = sqlite3.connect(':memory:')

# Load the DataFrame into the SQLite database as a table named 'sales'
# index=False prevents adding the DataFrame index as a column
# if_exists='replace' overwrites the table if it already exists
df.to_sql('sales', conn, index=False, if_exists='replace')

# First SQL query: Calculate total sales by region
# SELECT Region: Groups by the Region column
# SUM(Sales): Adds up all Sales values for each region
# AS TotalSales: Names the summed column
# FROM sales: Specifies the table to query
# GROUP BY Region: Groups the results by unique Region values
sql1 = "SELECT Region, SUM(Sales) AS TotalSales FROM sales GROUP BY Region"

# Execute the SQL query and print the results as a pandas DataFrame
print(pd.read_sql(sql1, conn))

# Second SQL query: Analyze sales trends by month
# strftime('%Y-%m', Date): Extracts year-month from the Date column
# AS Month: Names this extracted value as 'Month'
# SUM(Sales) AS MonthlySales: Sums sales for each month
# FROM sales: Specifies the table
# GROUP BY Month: Groups by the extracted month
# ORDER BY Month: Sorts results chronologically by month
sql2 = """
SELECT strftime('%Y-%m', Date) as Month, SUM(Sales) as MonthlySales
FROM sales
GROUP BY Month ORDER BY Month
"""

# Execute the query and print monthly sales trends
print(pd.read_sql(sql2, conn))

# Third SQL query: Find the best-selling products by quantity
# SELECT Product: Selects the Product column
# SUM(Quantity) AS TotalQuantity: Sums quantity for each product
# FROM sales: Specifies the table
# GROUP BY Product: Groups by unique product names
# ORDER BY TotalQuantity DESC: Sorts by total quantity in descending order (highest first)
sql3 = """
SELECT Product, SUM(Quantity) as TotalQuantity
FROM sales
GROUP BY Product
ORDER BY TotalQuantity DESC
"""

# Execute the query and print product quantity rankings
print(pd.read_sql(sql3, conn))

# Close the database connection to free up resources
conn.close()
