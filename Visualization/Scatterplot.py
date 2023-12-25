import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('../DataSets/FORTEBANK_tires_preprocessed.csv')

# Convert 'High' column to numeric values
data['High'] = pd.to_numeric(data['High'], errors='coerce')  # Use 'coerce' to handle non-numeric values

# Drop rows with missing or NaN values in 'High' column
data = data.dropna(subset=['High'])

# Scatterplot for Price vs. High
plt.scatter(data['High'], data['Price'], color='green', alpha=0.7)
plt.title('Price vs. High')
plt.xlabel('High')
plt.ylabel('Price')
plt.show()
