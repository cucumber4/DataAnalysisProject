import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tire_data = pd.read_csv('../DataSets/FORTEBANK_tires_preprocessed.csv')

plt.hist(tire_data['Price'], bins=20, color='blue', edgecolor='black')

plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Tire Prices')

plt.show()

plt.show()