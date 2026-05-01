import pandas as pd
import numpy as np

n = 12000
np.random.seed(0)

df = pd.DataFrame({
    'TransactionID': np.arange(1, n+1),
    'Date': pd.date_range('2025-01-01', periods=n, freq='H'),
    'Product': np.random.choice(['WidgetA', 'WidgetB', 'WidgetC'], n),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], n),
    'Sales': np.random.randint(20, 500, n),
    'Quantity': np.random.randint(1, 20, n)
})

df.to_csv('../data/sales_data.csv', index=False)
