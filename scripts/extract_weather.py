"""
Extract Weather Data for Kochi (ETL Step 1)

This script fetches live hourly weather data for Kochi using the
Open-Meteo API (no API key needed) and saves it into:

    Weather_ETL/data/raw/weather.json

Data pulled:
- temperature_2m
- relative_humidity_2m
- windspeed_10m
- time

Date: 22-Nov-2025
"""


import requests
import json
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract_weather():
    try:
        logging.info("Starting weather data extraction")

        latitude = 9.9312
        longitude = 76.2673

        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}"
            f"&hourly=temperature_2m,relative_humidity_2m,windspeed_10m"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises error if status != 200

        data = response.json()

        raw_folder = "../data/raw"
        os.makedirs(raw_folder, exist_ok=True)

        raw_file = os.path.join(raw_folder, "weather.json")

        with open(raw_file, "w") as f:
            json.dump(data, f, indent=4)

        logging.info("Weather data extracted and saved successfully")

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    extract_weather()