from data_processing import load_combined_data
import matplotlib.pyplot as plt
import seaborn as sns

# Load combined_data using the function from data_processing.py
combined_data = load_combined_data()

# Plot histograms for each numerical column
combined_data.hist(bins=30, figsize=(15, 10))
plt.suptitle('Histograms of All Numeric Columns')
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(combined_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# Scatter plots for selected columns
sns.pairplot(combined_data)
plt.show()
