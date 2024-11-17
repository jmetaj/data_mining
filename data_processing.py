import pandas as pd
import os

# Function to load and combine all CSV files into one DataFrame
def load_combined_data(data_path='harth'):
    csv_files = [f for f in os.listdir(data_path) if f.endswith('.csv')]
    dataframes = [pd.read_csv(os.path.join(data_path, file)) for file in csv_files]
    combined_data = pd.concat(dataframes, ignore_index=True)
    return combined_data

# Clean and remove unnecessary columns
def clean_combined_data(data_path='harth'):
    combined_data = load_combined_data(data_path)
    # Drop columns that are not needed
    columns_to_drop = ['index', 'Unnamed: 0']
    combined_data = combined_data.drop(columns=[col for col in columns_to_drop if col in combined_data.columns])
    return combined_data


if __name__ == "__main__":
    combined_data = clean_combined_data()
    
    
    print(combined_data.head())
    
    # Compute and display basic statistics 
    summary_stats = combined_data.describe()
    print(summary_stats)
