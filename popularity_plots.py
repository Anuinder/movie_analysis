# -*- coding: utf-8 -*-
"""
@author: Anu
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import utils

# import cleaned dataset
df = pd.read_csv('./movies_clean.csv', index_col = 0)

def popularity_traits_budget():
    '''Budget and popularity relationship'''
    
    budget_data = utils.group_creation(df['budget'])
    df['budget_group'] = pd.cut(df['budget'], budget_data[1], labels=budget_data[0], include_lowest = True)
    mean = df.groupby('budget_group')['popularity'].mean()
    median = df.groupby('budget_group')['popularity'].median()
    
    plt.bar(np.arange(len(mean)),mean, label='mean')
    plt.ylabel('popularity')
    plt.xlabel('budget groups')
    plt.title('Budget and Popularity relationships')
    plt.xticks(np.arange(len(mean)), median.index)
    plt.show()
    return None

def popularity_traits_revenue():
    '''Revenue and popularity relationship'''
    
    revenue_data = utils.group_creation(df['revenue'])
    df['revenue_group'] = pd.cut(df['revenue'], revenue_data[1], labels=revenue_data[0], include_lowest = True)
    mean = df.groupby('revenue_group')['popularity'].mean()
    median = df.groupby('revenue_group')['popularity'].median()
    
    plt.bar(np.arange(len(mean)),mean, label='mean')
    plt.ylabel('popularity')
    plt.xlabel('Revenue groups')
    plt.title('Revenue and Popularity relationships')
    plt.xticks(np.arange(len(mean)), median.index)
    plt.show()
    return None

def popularity_traits_runtime():
    '''Runtime and popularity relationship'''
    
    runtime_data = utils.group_creation(df['runtime'])
    df['runtime_group'] = pd.cut(df['runtime'], runtime_data[1], labels=runtime_data[0], include_lowest = True)
    mean = df.groupby('runtime_group')['popularity'].mean()
    median = df.groupby('runtime_group')['popularity'].median()
    
    plt.bar(np.arange(len(mean)),mean, label='mean')
    plt.ylabel('popularity')
    plt.xlabel('Runtime groups')
    plt.title('Runtime and Popularity relationships')
    plt.xticks(np.arange(len(mean)), median.index)
    plt.show()
    return None

def popularity_traits_earnings():
    '''Profit/Loss and popularity relationship'''
    
    earning_data = utils.group_creation(df['profit_loss'])
    df['pl_group'] = pd.cut(df['profit_loss'], earning_data[1], labels=earning_data[0], include_lowest = True)
    mean = df.groupby('pl_group')['popularity'].mean()
    median = df.groupby('pl_group')['popularity'].median()
    
    plt.bar(np.arange(len(mean)),mean, label='mean')
    plt.ylabel('popularity')
    plt.xlabel('Profit/Loss groups')
    plt.title('Profit/Loss and Popularity relationships')
    plt.xticks(np.arange(len(mean)), median.index)
    plt.show()
    return None

def popularity_traits_votes():
    '''Vote average and popularity relationship'''
    
    votes_data = utils.group_creation(df['vote_average']);
    df['va_group'] = pd.cut(df['vote_average'], votes_data[1], labels=votes_data[0], include_lowest = True)
    mean = df.groupby('va_group')['popularity'].mean()
    median = df.groupby('va_group')['popularity'].median()
    
    plt.bar(np.arange(len(mean)),mean, label='mean')
    plt.ylabel('popularity')
    plt.xlabel('Votes groups')
    plt.title('Votes/Loss and Popularity relationships')
    plt.xticks(np.arange(len(mean)), median.index)
    plt.show()
    return None

def revenue_budget():
    ''' budget level with high revenue movies'''
    
    budget_data = utils.group_creation(df['budget']);
    df['budget_group'] = pd.cut(df['budget'], budget_data[1], labels=budget_data[0], include_lowest = True)
    mean = df.groupby('budget_group')['revenue'].mean()
    median = df.groupby('budget_group')['revenue'].median()
    
    plt.bar(np.arange(len(mean)),mean, label='mean')
    plt.ylabel('Revenue')
    plt.xlabel('budget groups')
    plt.title('Budget and Revenue relationships')
    plt.xticks(np.arange(len(mean)), median.index)
    plt.show()
    return None

def popularity_cast():
    '''Cast, production company , genre of most popular movies'''
    
    dataframe = df.sort_values(['release_year','popularity'], ascending=[True, False])
    dataframe = dataframe.groupby('release_year').head(200).reset_index(drop=True)
    actor = utils.unqiues_from_multiples(dataframe['cast'])
    actor = pd.Series(actor, index = sorted(actor, key=actor.get, reverse=True)).head(10)
    #company = utils.unqiues_from_multiples(dataframe['production_companies'])
    #company = pd.Series(company, index = sorted(company, key=company.get, reverse=True)).head(20)
    #country = utils.unqiues_from_multiples(dataframe['production_countries'])
    #country = pd.Series(country, index = sorted(country, key=country.get, reverse=True)).head(20)
    genre = utils.unqiues_from_multiples(dataframe['genres'])
    genre = pd.Series(genre, index = sorted(genre, key=genre.get, reverse=True)).head(10)
    language = utils.unqiues_from_multiples(dataframe['spoken_languages'])
    language = pd.Series(language, index = sorted(language, key=language.get, reverse=True)).head(10)
    keyword = utils.unqiues_from_multiples(dataframe['keywords'])
    keyword = pd.Series(keyword, index = sorted(keyword, key=keyword.get, reverse=True)).head(10)
    
    dataframe = pd.DataFrame({'cast': actor.index, 'genres': genre.index, 'Language': language.index, 'Keywords':keyword.index})
    print(dataframe)
    return None

# budget and popularity relationship
popularity_traits_budget()

# revenue and popularity relationship
popularity_traits_revenue()

# profit/loss and popluarity relationship
popularity_traits_earnings()

# runtime and popluarity relationship
popularity_traits_runtime()

# vote averahe and popluarity relationship
popularity_traits_votes()

# budget level with high revenue movies
revenue_budget()

popularity_cast()