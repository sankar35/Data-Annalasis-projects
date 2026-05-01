import pandas as pd
import sqlite3

df = pd.read_csv('../data/sales_data.csv')
conn = sqlite3.connect(':memory:')
df.to_sql('sales', conn, index=False, if_exists='replace')

# Example SQL - Total sales by region
sql1 = "SELECT Region, SUM(Sales) AS TotalSales FROM sales GROUP BY Region"
print(pd.read_sql(sql1, conn))

# Trend - sales per month
sql2 = """
SELECT strftime('%Y-%m', Date) as Month, SUM(Sales) as MonthlySales
FROM sales
GROUP BY Month ORDER BY Month
"""
print(pd.read_sql(sql2, conn))

# Pattern - Best selling product
sql3 = """
SELECT Product, SUM(Quantity) as TotalQuantity
FROM sales
GROUP BY Product
ORDER BY TotalQuantity DESC
"""
print(pd.read_sql(sql3, conn))

conn.close()
