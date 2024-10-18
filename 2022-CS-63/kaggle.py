import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'app_store_reviews.csv'  
df = pd.read_csv(file_path, delimiter=';')  

print(df.head())

#  Basic operations
print("Missing values in each column:\n", df.isnull().sum())

print("Summary statistics:\n", df.describe())

print("Unique platforms:\n", df['platform'].unique())
print("Unique countries:\n", df['country'].unique())

country_reviews = df['country'].value_counts()
print("\nReviews by Country:\n", country_reviews)

star_distribution = df['star'].value_counts()
print("\nStar Rating Distribution:\n", star_distribution)

df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')

duplicates = df[df.duplicated(subset=['user_id', 'review'], keep=False)]
print("\nDuplicate reviews:\n", duplicates)

df = df.drop_duplicates(subset=['user_id', 'review'])


# Analysis

five_star_reviews = df[df['star'] == 5]
print("\nNumber of 5-star reviews:", five_star_reviews.shape[0])

avg_likes_dislikes = df.groupby('star')[['likes_count', 'dislike_count']].mean()
print("\nAverage likes and dislikes by star rating:\n", avg_likes_dislikes)

country_star_reviews = df.groupby(['country', 'star']).size().unstack(fill_value=0)
print("\nNumber of reviews by country and star rating:\n", country_star_reviews)


# Visualizations

plt.figure(figsize=(10, 6))
country_reviews.plot(kind='bar', color='skyblue')
plt.title('Number of Reviews by Country')
plt.xlabel('Country')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
star_distribution.plot(kind='bar', color='coral')
plt.title('Star Rating Distribution')
plt.xlabel('Star Rating')
plt.ylabel('Number of Reviews')
plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 6))
plt.plot(avg_likes_dislikes.index, avg_likes_dislikes['likes_count'], marker='o', color='green', label='Average Likes')
plt.plot(avg_likes_dislikes.index, avg_likes_dislikes['dislike_count'], marker='o', color='red', label='Average Dislikes')
plt.title('Average Likes and Dislikes by Star Rating')
plt.xlabel('Star Rating')
plt.ylabel('Average Count')
plt.legend()
plt.tight_layout()
plt.show()

