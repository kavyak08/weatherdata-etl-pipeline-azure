"""
Transform Weather Data (ETL Step 2)

This script reads the raw weather JSON file generated during the Extract step.
It selects key fields such as time, temperature, humidity, and windspeed,
converts them into a clean table format using pandas, and stores the result as:

    Weather_ETL/data/cleaned/weather_cleaned.csv

Purpose of Transform Step:
- Clean raw JSON
- Keep only useful columns
- Convert to tabular CSV for loading into databases or dashboards

Author: Kavya K
Date: 22-Nov-2025
"""


import json
import os
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def transform_weather():
    logging.info("Starting weather data transformation")

    raw_file = "../data/raw/weather.json"
    cleaned_folder = "../data/cleaned"

    # Validation 1: Check if raw file exists
    if not os.path.exists(raw_file):
        logging.error("Raw weather.json file not found. Run extract step first.")
        return

    try:
        # Read raw JSON
        with open(raw_file, "r") as f:
            data = json.load(f)

        # Validation 2: Check expected structure
        if "hourly" not in data:
            logging.error("Invalid JSON structure: 'hourly' key not found")
            return

        hourly = data["hourly"]

        # Create DataFrame
        df = pd.DataFrame({
            "time": hourly["time"],
            "temperature": hourly["temperature_2m"],
            "humidity": hourly["relative_humidity_2m"],
            "wind_speed": hourly["windspeed_10m"]
        })

        # Ensure cleaned folder exists
        os.makedirs(cleaned_folder, exist_ok=True)

        cleaned_file = os.path.join(cleaned_folder, "weather_cleaned.csv")
        df.to_csv(cleaned_file, index=False)

        logging.info(f"Weather data transformed successfully: {cleaned_file}")

    except Exception as e:
        logging.error(f"Error during transformation: {e}")

if __name__ == "__main__":
    transform_weather()