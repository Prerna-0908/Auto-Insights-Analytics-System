import pandas as pd
def clean_data(file_path):

    data = pd.read_csv(file_path)

    # Convert dates
    data['Order Date'] = pd.to_datetime(data['Order Date'],dayfirst=True, errors='coerce')
    data['Ship Date'] = pd.to_datetime(data['Ship Date'],dayfirst=True, errors='coerce')

    # Handle missing values
    data['Postal Code'] = data['Postal Code'].fillna(0)

    return data