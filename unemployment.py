import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
data = pd.read_csv("unemployment.csv")

# Fix column name spaces
data.columns = data.columns.str.strip()

print(data.head())
print(data.info())

# Convert Date column
data['Date'] = pd.to_datetime(data['Date'])

print(data.isnull().sum())
print(data.describe())

# Trend
plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=data)
plt.title("Unemployment Rate Over Time")
plt.show()

# Covid impact
covid_data = data[data['Date'].dt.year == 2020]
plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=covid_data)
plt.title("Covid-19 Impact on Unemployment")
plt.show()

# Seasonal
data['Month'] = data['Date'].dt.month
plt.figure(figsize=(10,5))
sns.boxplot(x='Month', y='Estimated Unemployment Rate (%)', data=data)
plt.title("Seasonal Unemployment Trend")
plt.show()

