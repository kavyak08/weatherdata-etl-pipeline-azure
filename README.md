# Weather Data ETL Pipeline using Azure SQL

This project demonstrates an end-to-end ETL pipeline built using Python and Azure SQL Database.

## Project Overview

This pipeline performs:

Extract  
Fetches live weather data from Open-Meteo API (Kochi location)

Transform  
Cleans and converts JSON data into structured CSV format using pandas

Load  
Loads cleaned data into Azure SQL Database using SQLAlchemy and PyODBC

## Tech Stack

Python  
Pandas  
Azure SQL Database  
SQLAlchemy  
PyODBC  
REST API  
Logging  

## Project Structure

Weather_ETL/
│
├── scripts/
│ ├── extract_weather.py
│ ├── transform_weather.py
│ └── load_weather.py
│
├── data/
│ ├── raw/
│ └── cleaned/
│
├── logs/
│
└── README.md

## Features

Secure credential handling using environment variables  
Logging implemented for monitoring  
Cloud database integration  

## Author

Kavya K