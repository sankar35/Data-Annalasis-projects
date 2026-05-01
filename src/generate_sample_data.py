# Import necessary modules
from pathlib import Path  # For handling file paths in a cross-platform way

import numpy as np  # NumPy for numerical operations and random number generation
import pandas as pd  # Pandas for data manipulation and creating DataFrames

# Construct the output directory path
# __file__ gives the path to this script file
# .resolve() gets the absolute path
# .parent.parent goes up two directories (from src/ to project root)
# Then append 'data' to create the data directory path
output_dir = Path(__file__).resolve().parent.parent / 'data'

# Create the output directory if it doesn't exist
# exist_ok=True prevents an error if the directory already exists
output_dir.mkdir(exist_ok=True)

# Construct the full path to the output CSV file
output_path = output_dir / 'sales_data.csv'

# Set the number of sample data rows to generate
n = 12000

# Set the random seed for reproducible results
# This ensures the same random data is generated each time the script runs
np.random.seed(0)

# Create a pandas DataFrame with sample sales data
# Each column represents a different aspect of sales transactions
df = pd.DataFrame({
    # TransactionID: Unique identifier for each transaction (1 to n)
    'TransactionID': np.arange(1, n+1),

    # Date: Hourly timestamps starting from 2025-01-01 for n periods
    # freq='h' means hourly frequency
    'Date': pd.date_range('2025-01-01', periods=n, freq='h'),

    # Product: Randomly chosen product names from the list
    # Each transaction gets one of WidgetA, WidgetB, or WidgetC
    'Product': np.random.choice(['WidgetA', 'WidgetB', 'WidgetC'], n),

    # Region: Randomly chosen region names from the list
    # Each transaction is assigned to one of North, South, East, or West
    'Region': np.random.choice(['North', 'South', 'East', 'West'], n),

    # Sales: Random integer sales amounts between 20 and 499 (inclusive)
    # Represents the dollar amount of each sale
    'Sales': np.random.randint(20, 500, n),

    # Quantity: Random integer quantities between 1 and 19 (inclusive)
    # Represents the number of items sold in each transaction
    'Quantity': np.random.randint(1, 20, n)
})

# Save the DataFrame to a CSV file
# index=False prevents pandas from writing row indices to the file
df.to_csv(output_path, index=False)
