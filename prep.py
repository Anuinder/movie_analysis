# -*- coding: utf-8 -*-
"""
@author: Anu
"""


'''
Based on preparation jupyter file
'''
import numpy as np
import pandas as pd

# dataset
df = pd.read_csv('./tmdb_movie_dataset.csv', index_col = 0)

# Dropping columns not necessary for now
df.drop(['homepage','overview','tagline','movie_id'],axis=1, inplace=True)

# drop the columns with missing data
df.replace([np.inf, -np.inf], np.nan, inplace = True)
df = df.dropna()

# extract date from release_date and add new column for it
df['release_year'] = pd.DatetimeIndex(df['release_date']).year

# drop release date
df.drop('release_date',axis=1, inplace=True)

# create a column for profit
df['profit_loss'] = df['revenue'] - df['budget']

# For now I am keeping rows with zero values

# save cleaned data for futher analysis
df.to_csv("movies_clean.csv")

