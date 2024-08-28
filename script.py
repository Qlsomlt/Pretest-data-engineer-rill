import pandas as pd

# Load data
df = pd.read_csv('review-lazada.csv')

# Explore data
print(df.head())
print(df.describe())
print(df.isnull().sum())

# drop original rating
df.drop(columns=['originalRating'], inplace=True)

# mengubah nama menjadi huruf kecil
df['name'] = df['name'].str.lower()

# print data
df.to_csv('cleaned_data.csv', index=False)