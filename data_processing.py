import pandas as pd
import os

# Function to load and combine all CSV files into one DataFrame
def load_combined_data(data_path='harth'):
    csv_files = [f for f in os.listdir(data_path) if f.endswith('.csv')]
    dataframes = [pd.read_csv(os.path.join(data_path, file)) for file in csv_files]
    combined_data = pd.concat(dataframes, ignore_index=True)
    return combined_data

# Main block to load data and print stats if running this script directly
if __name__ == "__main__":
    combined_data = load_combined_data()
    
    # Display the first few rows
    print(combined_data.head())
    
    # Compute and display basic statistics
    summary_stats = combined_data.describe()
    print(summary_stats)
