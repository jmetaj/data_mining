from data_processing import clean_combined_data  
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean data 
combined_data = clean_combined_data()

sampled_data = combined_data.sample(n=1000, random_state=42)

# Ensure only numeric data is used 
numeric_data = combined_data.select_dtypes(include=['number'])

combined_data.hist(bins=30, figsize=(15, 10))
plt.suptitle('Histograms of All Numeric Columns')
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Scatter plots 
sns.pairplot(sampled_data)
plt.show()

