"""
Weather_ETL Project Folder Creator

This script automatically creates the folder structure for the Weather ETL project.
It is designed to help set up the project quickly and avoid manual folder creation.

Folder Structure Created:
Weather_ETL/
    data/
        raw/        - Store raw CSV or API data
        cleaned/    - Store cleaned/transformed data
    scripts/       - Python scripts for ETL (extract, transform, load)
    notebooks/     - Jupyter notebooks for analysis/visualization
    README.md      - Project overview and instructions

How to Use:
1. Save this script as `create_folders.py`.
2. Run the script using Python:
    python create_folders.py
3. The folder structure will be created in the current working directory.
4. You can now add your ETL scripts, data files, and notebooks in the appropriate folders.

Author: Kavya K
Date: 21-Nov-2025
"""


import os

# Define main project folder
project_folder = "Weather_ETL"

# Subfolders
subfolders = [
    "data/raw",
    "data/cleaned",
    "scripts",
    "notebooks"
]

# Create main folder
os.makedirs(project_folder, exist_ok=True)

# Create subfolders
for folder in subfolders:
    os.makedirs(os.path.join(project_folder, folder), exist_ok=True)

# Create empty README.md
with open(os.path.join(project_folder, "README.md"), "w") as f:
    f.write("# Weather ETL Project\n\nProject description goes here.")

print("Folder structure created successfully!")
