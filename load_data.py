import pandas as pd
import os


data_path = 'harth'


csv_files = [f for f in os.listdir(data_path) if f.endswith('.csv')]

# Load and combine all CSV files into one DataFrame 
dataframes = [pd.read_csv(os.path.join(data_path, file)) for file in csv_files]
combined_data = pd.concat(dataframes, ignore_index=True)

# Display the first few rows 
print(combined_data.head())
