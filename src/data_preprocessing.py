# src/data_preprocessing.py

import pandas as pd

def load_data(sheet_name):
    # Load data from specified sheet in Excel file
    file_path = 'data/survey_data.xlsx'
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    return data

def clean_data(data):
    # Basic cleaning: Strip column names and handle missing values if needed
    data.columns = [col.strip() for col in data.columns]
    return data
