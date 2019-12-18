#%%
# Generate movie ratings from the 25 Million dataset
import os 
import pandas as pd

all_ratings = pd.read_csv("dataset/ratings.csv",header = 1, delimiter = ",", names = ["UserID", "MovieID", "Rating", "Datetime"] )

#%% Apriori: If a person recommends these movies, they will also recommend this movies

# Generate favourable ratings column for ratings > 3
all_ratings['Favorable'] = all_ratings['Rating'] > 3

# Split into training 

ratings = all_ratings[all_ratings['UserID'].isin(range(200))]
favorable_ratings = ratings[ratings["Favorable"]]
favorable_reviews_by_users = dict((k, frozenset(v.values))for k, v in favorable_ratings.groupby("UserID")["MovieID"])



