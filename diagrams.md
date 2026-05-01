# Project Diagrams

This document contains flowcharts and design diagrams for the Business Data Analysis Project.

## Overall Project Workflow

```mermaid
graph TD
    A[Start] --> B[Run generate_sample_data.py]
    B --> C[Generate sales_data.csv]
    C --> D[Choose Analysis Type]
    D --> E[Run data_analysis.py]
    D --> F[Run sql_analysis.py]
    E --> G[Pandas Analysis Output]
    F --> H[SQL Analysis Output]
    G --> I[End]
    H --> I
```

## Data Generation Flow (generate_sample_data.py)

```mermaid
flowchart TD
    A[Start Script] --> B[Import Modules: Path, numpy, pandas]
    B --> C[Set output directory path]
    C --> D[Create data directory if not exists]
    D --> E[Set number of rows: n = 12000]
    E --> F[Set random seed for reproducibility]
    F --> G[Create DataFrame with columns:]
    G --> H[TransactionID: 1 to n]
    G --> I[Date: Hourly timestamps]
    G --> J[Product: Random choice from WidgetA/B/C]
    G --> K[Region: Random choice from North/South/East/West]
    G --> L[Sales: Random int 20-499]
    G --> M[Quantity: Random int 1-19]
    H --> N[Save DataFrame to CSV]
    I --> N
    J --> N
    K --> N
    L --> N
    M --> N
    N --> O[End Script]
```

## Pandas Data Analysis Flow (data_analysis.py)

```mermaid
flowchart TD
    A[Start Script] --> B[Import Modules: Path, pandas]
    B --> C[Construct CSV file path]
    C --> D[Load CSV into DataFrame with parse_dates]
    D --> E[Print total number of rows]
    E --> F[Print summary statistics for Sales and Quantity]
    F --> G[Calculate top 5 products by total sales]
    G --> H[Print top products]
    H --> I[Calculate sales by region]
    I --> J[Print regional sales]
    J --> K[Set Date as index for time series]
    K --> L[Resample by month-end and sum sales]
    L --> M[Print monthly sales trend]
    M --> N[End Script]
```

## SQL Analysis Flow (sql_analysis.py)

```mermaid
flowchart TD
    A[Start Script] --> B[Import Modules: Path, pandas, sqlite3]
    B --> C[Construct CSV file path]
    C --> D[Load CSV into DataFrame]
    D --> E[Create in-memory SQLite connection]
    E --> F[Load DataFrame into 'sales' table]
    F --> G[Execute SQL Query 1: Total sales by region]
    G --> H[Print query results]
    H --> I[Execute SQL Query 2: Monthly sales trend]
    I --> J[Print query results]
    J --> K[Execute SQL Query 3: Best selling products by quantity]
    K --> L[Print query results]
    L --> M[Close database connection]
    M --> N[End Script]
```

## Data Flow Diagram

```mermaid
graph LR
    A[generate_sample_data.py] --> B[sales_data.csv]
    B --> C[data_analysis.py]
    B --> D[sql_analysis.py]
    C --> E[Pandas Analysis Results]
    D --> F[SQL Analysis Results]
```

## Class Diagram (Simplified)

```mermaid
classDiagram
    class DataGenerator {
        +generate_sample_data()
        +create_dataframe()
        +save_to_csv()
    }
    class PandasAnalyzer {
        +load_data()
        +calculate_statistics()
        +analyze_trends()
        +group_by_categories()
    }
    class SQLAnalyzer {
        +load_to_database()
        +execute_queries()
        +format_results()
    }
    DataGenerator --> sales_data.csv
    sales_data.csv --> PandasAnalyzer
    sales_data.csv --> SQLAnalyzer
```