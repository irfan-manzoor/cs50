import pandas as pd

def load_csv(filepath):
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def validate_data(data):
    if not all(col in data.columns for col in ["heart_rate", "blood_glucose", "temperature", "blood_pressure"]):
        print("Invalid CSV format.")
        return False
    return True
