import pandas as pd


df = pd.read_csv('review-lazada.csv')

# Explore data
print(df.head())
print(df.describe())
print(df.isnull().sum())


bad = df[(df['rating'] < 2)]
netral = df[(df['rating'] == 3)]
bagus= df[(df['rating'] > 3)]


print('hasil:')
print(bad)
print(netral)
print(bagus)