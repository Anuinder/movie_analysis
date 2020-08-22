# -*- coding: utf-8 -*-
"""
@author: Anu
"""

'''

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# import cleaned dataset
df = pd.read_csv('./movies_clean.csv', index_col = 0)

def no_movies_per_year_trend():
    '''Number of movies released per year.'''
    
    number = df.groupby('release_year').count()['id']
    plt.figure(figsize = (18,7))
    plt.title('No of movies released per year')
    plt.xlabel('Year')
    plt.ylabel('No of movies')
    number.plot(xticks = np.arange(number.index[0],number.index[-1],5))
    
    return None

def movie_profit_trends():
    ''' Profit of movies over the years'''
    
    rate = df.groupby('release_year')['profit_loss'].mean()
    plt.title("Profit rate over years")
    plt.xlabel('Release year')
    plt.ylabel('Mean Profit')
    plt.figure(figsize = (18,7))
    rate.plot()
   
    return None

def movie_runtime_trends():
    ''' Runtime of movies over years'''
    
    rate = df.groupby('release_year')['runtime'].mean()
    plt.title("Runtime rate over years")
    plt.xlabel('Release year')
    plt.ylabel('Mean Runtime')
    plt.figure(figsize = (18,7))
    rate.plot()
   
    return None    

def movie_popularity_trends():
    ''' Popularity of movies over years'''
    
    rate = df.groupby('release_year')['popularity'].mean()
    plt.title("Popularity over years")
    plt.xlabel('Release year')
    plt.ylabel('Mean Popularity')
    plt.figure(figsize = (18,7))
    rate.plot()
   
    return None 

def movie_budget_trends():
    ''' Budget of movies over years'''
    
    rate = df.groupby('release_year')['budget'].mean()
    #print(rate)
    plt.title("Budget over years")
    plt.xlabel('Release year')
    plt.ylabel('Mean Budget')
    plt.figure(figsize = (18,7))
    rate.plot()
   
    return None 

# no of movies released per year
no_movies_per_year_trend()
#movies trends based on profits
movie_profit_trends()
#movie trends based on runtime
movie_runtime_trends()
#movie trends based on popularity
movie_popularity_trends()
#movie trends based on budget
movie_budget_trends()