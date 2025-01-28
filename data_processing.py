import pandas as pd
import os
from sklearn.preprocessing import StandardScaler  

def load_combined_data(data_path='harth'):
   
    csv_files = [f for f in os.listdir(data_path) if f.endswith('.csv')]
    dataframes = [pd.read_csv(os.path.join(data_path, file)) for file in csv_files]
    combined_data = pd.concat(dataframes, ignore_index=True)
    return combined_data

def clean_combined_data(data_path='harth'):
    
    combined_data = load_combined_data(data_path)

    # remove unnecessary columns 
    columns_to_drop = ['index', 'Unnamed: 0']
    combined_data = combined_data.drop(columns=[col for col in columns_to_drop if col in combined_data.columns])

    combined_data = combined_data.dropna()

    # normelize
    numeric_columns = combined_data.select_dtypes(include=['number']).columns  
    scaler = StandardScaler()  
    combined_data[numeric_columns] = scaler.fit_transform(combined_data[numeric_columns])

    return combined_data

if __name__ == "__main__":

    combined_data = clean_combined_data()
    
    print("First rows of combined data after normalization:")
    print(combined_data.head())
    
    summary_stats = combined_data.describe()
    print("\nBasic Statistics After Normalization:")
    print(summary_stats)
