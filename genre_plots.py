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

def most_common_genre():
    ''' Most common of genres over years'''
    
    total_genre_count = utils.unqiues_from_multiples(df['genres'])
    total_genre_count = pd.DataFrame(total_genre_count.items(), columns = ['genre_name','movie_count'])
    names = total_genre_count['genre_name']
    count = total_genre_count['movie_count']
    
    plt.barh(names,count)
    plt.title("Most common genre over years")
    plt.xlabel('Number Of Movies')
    plt.ylabel("Genres")
    plt.show()

    return None 

def genre_trend_decades():
    ''' Popularity of genres over decades'''
    
    unique_years = np.sort(df['release_year'].unique())
    before_1940s = utils.no_values_in_range(unique_years,unique_years[0],1940)
    in_40s_60s =  utils.no_values_in_range(unique_years,1940,1960)
    in_60s_80s =  utils.no_values_in_range(unique_years,1960,1980)
    in_80s_2000s = utils.no_values_in_range(unique_years,1880,2000)
    after_2000s = utils.no_values_in_range(unique_years,2000,unique_years[-1])
    year_div_count = [ unique_years[:before_1940s],
                      unique_years[before_1940s:in_40s_60s],
                      unique_years[in_40s_60s:in_60s_80s],
                      unique_years[in_60s_80s:in_80s_2000s],
                      unique_years[after_2000s:]
                      ]
    year_div_name = ['before_1940s','in_40s_60s','in_60s_80s','in_80s_2000s','after_2000s']
        
    dataframe = pd.DataFrame()
    index = 0
    for time in year_div_count:
        temp = df[df['release_year'].isin(time)]
        genre_count = utils.unqiues_from_multiples(temp['genres'])
        #print('-----',genre_count)
        genre_count = pd.Series(genre_count, index = sorted(genre_count, key=genre_count.get, reverse=True))
        #print(genre_count.head())
        temp =pd.DataFrame({'year' :year_div_name[index],'top': genre_count.head(1)})
        index = index + 1
        dataframe = dataframe.append(temp)
    
    fig, ax1 = plt.subplots()
    ax1.barh(np.arange(len(year_div_name)),dataframe['top'])
    ax1.set_yticks(np.arange(len(year_div_name)))
    ax1.set_yticklabels(dataframe.index)
    ax1.set_ylabel('Genres')
    
    ax2 = ax1.twinx()
    ax2.barh(np.arange(len(year_div_name)),dataframe['top'])
    ax2.set_yticks(np.arange(len(year_div_name)))
    ax2.set_yticklabels(year_div_name)
    ax2.set_ylabel('Years')
    
    plt.title(" genre trends over year")
    plt.show()
    
    return None


# genre with highest release of movies
most_common_genre()

# genre trends over decades
genre_trend_decades()