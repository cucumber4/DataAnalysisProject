import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('../DataSets/FORTEBANK_tires.csv')

# Filter rows with valid 'Season' values
valid_seasons = ['Летние', 'Зимние', 'Всесезонные']  # Adjust the list based on your valid season values
filtered_data = data[data['Season'].isin(valid_seasons)]

# Plot the count of tires for each season
season_counts = filtered_data['Season'].value_counts()
season_counts.plot(kind='bar', color='green', alpha=0.7)
plt.title('Count of Tires for Each Season')
plt.xlabel('Season')
plt.ylabel('Count')
plt.show()
