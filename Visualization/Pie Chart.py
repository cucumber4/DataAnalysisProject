import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('../DataSets/FORTEBANK_tires_preprocessed.csv')

# Plot the distribution of tire brands using a pie chart
brand_distribution = data['Brand'].value_counts()
plt.pie(brand_distribution, labels=brand_distribution.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribution of Tire Brands')
plt.show()
