# Data Cleaning and Preprocessing Script
# This script demonstrates end-to-end data cleaning and preprocessing
# using Python libraries (Pandas, NumPy) to ensure data accuracy and consistency

from pathlib import Path
import pandas as pd
import numpy as np

# Set up paths
project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / 'cleaning_samples'
output_dir = project_root / 'cleaned_data'
output_dir.mkdir(exist_ok=True)

print("Starting data cleaning and preprocessing...")

# Function to clean sales data
def clean_sales_data():
    print("\n1. Cleaning Sales Data...")

    # Load raw sales data
    sales_df = pd.read_csv(data_dir / 'raw_sales_data.csv', parse_dates=['Date'])

    print(f"Original sales data shape: {sales_df.shape}")
    print(f"Missing values:\n{sales_df.isnull().sum()}")

    # Remove duplicates
    sales_df = sales_df.drop_duplicates()
    print(f"After removing duplicates: {sales_df.shape}")

    # Handle missing values
    # Fill missing Sales with median
    sales_df['Sales'] = sales_df['Sales'].fillna(sales_df['Sales'].median())

    # Fill missing Quantity with mean
    sales_df['Quantity'] = sales_df['Quantity'].fillna(sales_df['Quantity'].mean())

    # Ensure data types are correct
    sales_df['TransactionID'] = sales_df['TransactionID'].astype(int)
    sales_df['Sales'] = sales_df['Sales'].astype(float)
    sales_df['Quantity'] = sales_df['Quantity'].astype(int)

    # Remove outliers (sales > 3 standard deviations from mean)
    sales_mean = sales_df['Sales'].mean()
    sales_std = sales_df['Sales'].std()
    sales_df = sales_df[sales_df['Sales'] <= sales_mean + 3 * sales_std]

    print(f"Final sales data shape: {sales_df.shape}")
    print(f"Data types:\n{sales_df.dtypes}")

    # Save cleaned data
    sales_df.to_csv(output_dir / 'cleaned_sales_data.csv', index=False)
    print("Cleaned sales data saved.")

    return sales_df

# Function to clean customer data
def clean_customer_data():
    print("\n2. Cleaning Customer Data...")

    # Load raw customer data
    customer_df = pd.read_csv(data_dir / 'raw_customer_data.csv', parse_dates=['RegistrationDate'])

    print(f"Original customer data shape: {customer_df.shape}")
    print(f"Missing values:\n{customer_df.isnull().sum()}")

    # Handle missing phone numbers
    customer_df['Phone'] = customer_df['Phone'].fillna('Not Provided')

    # Standardize phone format (assuming US format)
    def format_phone(phone):
        if phone == 'Not Provided':
            return phone
        # Remove all non-digit characters
        digits = ''.join(filter(str.isdigit, phone))
        if len(digits) == 10:
            return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        return phone

    customer_df['Phone'] = customer_df['Phone'].apply(format_phone)

    # Ensure age is reasonable (18-100)
    customer_df['Age'] = customer_df['Age'].clip(18, 100)

    # Standardize city names (title case)
    customer_df['City'] = customer_df['City'].str.title()

    # Remove any duplicate customer IDs
    customer_df = customer_df.drop_duplicates(subset=['CustomerID'])

    print(f"Final customer data shape: {customer_df.shape}")
    print(f"Data types:\n{customer_df.dtypes}")

    # Save cleaned data
    customer_df.to_csv(output_dir / 'cleaned_customer_data.csv', index=False)
    print("Cleaned customer data saved.")

    return customer_df

# Function to clean product data
def clean_product_data():
    print("\n3. Cleaning Product Data...")

    # Load raw product data
    product_df = pd.read_csv(data_dir / 'raw_product_data.csv')

    print(f"Original product data shape: {product_df.shape}")
    print(f"Missing values:\n{product_df.isnull().sum()}")

    # Handle missing stock values
    product_df['Stock'] = product_df['Stock'].fillna(product_df['Stock'].median())

    # Ensure data types
    product_df['Price'] = product_df['Price'].astype(float)
    product_df['Stock'] = product_df['Stock'].astype(int)

    # Standardize category names
    category_mapping = {
        'Electronics': 'Electronics',
        'Home & Garden': 'Home & Garden',
        'Books': 'Books'
    }
    product_df['Category'] = product_df['Category'].map(category_mapping)

    # Remove products with negative or zero price
    product_df = product_df[product_df['Price'] > 0]

    # Remove products with negative stock
    product_df = product_df[product_df['Stock'] >= 0]

    print(f"Final product data shape: {product_df.shape}")
    print(f"Data types:\n{product_df.dtypes}")

    # Save cleaned data
    product_df.to_csv(output_dir / 'cleaned_product_data.csv', index=False)
    print("Cleaned product data saved.")

    return product_df

# Function to validate cleaned data
def validate_cleaned_data(sales_df, customer_df, product_df):
    print("\n4. Validating Cleaned Data...")

    # Check for data integrity
    print("Sales data validation:")
    print(f"- No missing values: {sales_df.isnull().sum().sum() == 0}")
    print(f"- All sales positive: {(sales_df['Sales'] > 0).all()}")
    print(f"- All quantities positive: {(sales_df['Quantity'] > 0).all()}")

    print("Customer data validation:")
    print(f"- No missing critical fields: {customer_df[['CustomerID', 'Name', 'Email']].isnull().sum().sum() == 0}")
    print(f"- Ages within range: {customer_df['Age'].between(18, 100).all()}")

    print("Product data validation:")
    print(f"- No missing values: {product_df.isnull().sum().sum() == 0}")
    print(f"- All prices positive: {(product_df['Price'] > 0).all()}")
    print(f"- All stock non-negative: {(product_df['Stock'] >= 0).all()}")

# Main execution
if __name__ == "__main__":
    try:
        # Clean all datasets
        sales_cleaned = clean_sales_data()
        customer_cleaned = clean_customer_data()
        product_cleaned = clean_product_data()

        # Validate the cleaned data
        validate_cleaned_data(sales_cleaned, customer_cleaned, product_cleaned)

        print("\n✅ Data cleaning and preprocessing completed successfully!")
        print(f"Cleaned files saved in: {output_dir}")

    except Exception as e:
        print(f"❌ Error during data cleaning: {e}")
        raise