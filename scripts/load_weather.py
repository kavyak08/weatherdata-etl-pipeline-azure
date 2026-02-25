"""
Load Weather Data into Azure SQL Database (ETL Step 3)

This script reads the cleaned CSV file generated during the Transform step
and inserts it into an Azure SQL Database table named 'weather_data'.

Author: Kavya K
Date: 24-Nov-2025
"""


import pandas as pd
import os
import logging
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_weather():
    logging.info("Starting data load into Azure SQL")

    # Path to cleaned CSV
    cleaned_file = "../data/cleaned/weather_cleaned.csv"

    # Validation 1: Check CSV exists
    if not os.path.exists(cleaned_file):
        logging.error("Cleaned CSV not found. Run transform step first.")
        return

    try:
        # Read cleaned data
        df = pd.read_csv(cleaned_file)
        logging.info(f"Read {len(df)} rows from cleaned CSV")

        # Azure SQL connection details
        server = "kavya-weather-sql.database.windows.net"
        database = "weatherdb"
        username = "sqladmin"
        password = "Kodanchery@0803"

        connection_string = (
            f"mssql+pyodbc://{username}:{password}@{server}:1433/"
            f"{database}?driver=ODBC+Driver+18+for+SQL+Server"
        )

        # Create engine
        engine = create_engine(connection_string)

        # Load data
        df.to_sql("weather_data", engine, if_exists="replace", index=False)

        logging.info("Weather data successfully loaded into Azure SQL")

    except Exception as e:
        logging.error(f"Failed to load data into Azure SQL: {e}")

if __name__ == "__main__":
    load_weather()