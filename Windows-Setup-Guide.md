# Windows Setup Guide for Data Analysis Project

This guide provides step-by-step instructions to set up the environment on a Windows machine, clone the repository, and run the Python scripts for the Business Data Analysis Project.

## Prerequisites

- Windows 10 or later
- Internet connection
- Administrator privileges for installations

## Step 1: Install Git

1. Download Git from the official website: https://git-scm.com/download/win
2. Run the installer and follow the default installation options.
3. Open Command Prompt or PowerShell and verify installation:
   ```
   git --version
   ```

## Step 2: Install Python

1. Download Python from the official website: https://www.python.org/downloads/
2. Choose the latest stable version (3.8 or higher recommended).
3. During installation, make sure to check "Add Python to PATH".
4. Open Command Prompt and verify installation:
   ```
   python --version
   pip --version
   ```

## Step 3: Install GitHub Desktop (Optional but Recommended)

1. Download GitHub Desktop from: https://desktop.github.com/
2. Install and sign in with your GitHub account.
3. This provides a GUI for cloning and managing repositories.

## Step 4: Clone the Repository

### Using GitHub Desktop:
1. Open GitHub Desktop.
2. Click "File" > "Clone repository".
3. Search for "sankar35/Data-Annalasis-projects" or paste the URL: https://github.com/sankar35/Data-Annalasis-projects
4. Choose a local path and click "Clone".

### Using Command Line:
1. Open Command Prompt or PowerShell.
2. Navigate to your desired directory:
   ```
   cd C:\Users\YourUsername\Documents
   ```
3. Clone the repository:
   ```
   git clone https://github.com/sankar35/Data-Annalasis-projects.git
   ```
4. Navigate into the cloned directory:
   ```
   cd Data-Annalasis-projects
   ```

## Step 5: Install Project Dependencies

1. In the project directory, install the required packages:
   ```
   pip install -r requirements.txt
   ```
2. Verify installations:
   ```
   python -c "import pandas, numpy, sqlite3; print('Dependencies installed successfully')"
   ```

## Step 6: Run the Python Scripts

Run each script in sequence from the project root directory:

1. **Generate Sample Data**:
   ```
   python src/generate_sample_data.py
   ```
   This creates `data/sales_data.csv` with 12,000 rows of sample sales data.

2. **Run Pandas Data Analysis**:
   ```
   python src/data_analysis.py
   ```
   This performs summary statistics, grouping, and trend analysis using pandas.

3. **Run SQL Analysis**:
   ```
   python src/sql_analysis.py
   ```
   This loads the data into SQLite and performs SQL queries for insights.

## Expected Output

- **generate_sample_data.py**: Creates the CSV file (no console output)
- **data_analysis.py**: Displays data summary, top products, regional sales, and monthly trends
- **sql_analysis.py**: Shows SQL query results for regional sales, monthly trends, and product quantities

## Troubleshooting

- If you get "ModuleNotFoundError", ensure dependencies are installed correctly.
- If scripts fail to find the data file, ensure you're running from the project root directory.
- For permission issues, run Command Prompt as Administrator.

## Project Structure

```
Data-Annalasis-projects/
├── README.md
├── requirements.txt
├── data/
│   └── sales_data.csv (generated)
└── src/
    ├── generate_sample_data.py
    ├── data_analysis.py
    └── sql_analysis.py
```

## Additional Notes

- The project analyzes business sales data using both pandas and SQL approaches.
- All scripts are designed to run from the project root directory.
- The data directory will be created automatically when running the first script.</content>
<parameter name="filePath">/workspaces/Data-Annalasis-projects/Windows-Setup-Guide.md