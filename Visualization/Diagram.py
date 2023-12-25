import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('../DataSets/FORTEBANK_tires.csv')

# Map 'Spikes' column values to 1 for spiked and 0 for non-spiked
data['Spikes'] = data['Spikes'].map({'Есть': 1, 'Нет': 0})

# Plot the count of spiked vs. non-spiked tires
spikes_counts = data['Spikes'].value_counts()
spikes_counts.plot(kind='bar', color=['blue', 'red'], alpha=0.7)
plt.title('Count of Spiked vs. Non-Spiked Tires')
plt.xlabel('Spikes')
plt.ylabel('Count')
plt.xticks([0, 1], ['Non-Spiked', 'Spiked'], rotation=0)
plt.show()
