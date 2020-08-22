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

def most_common_actor():
    ''' Actor with maximum releases over the years'''
    
    total_actor_count = utils.unqiues_from_multiples(df['cast'])
    total_actor_count = pd.Series(total_actor_count, index = sorted(total_actor_count, key=total_actor_count.get, reverse=True)).head(20)
    #print(total_actor_count)
    names = total_actor_count.index
    count = total_actor_count.values
    
    plt.barh(names,count)
    plt.title("Frequently appearing actor over the years")
    plt.xlabel('Number Of Movies')
    plt.ylabel("Actor name")
    plt.show()

    return None 

def most_common_company():
    ''' Production company with maximum releases over the years'''
    
    total_company_count = utils.unqiues_from_multiples(df['production_companies'])
    total_company_count = pd.Series(total_company_count, index = sorted(total_company_count, key=total_company_count.get, reverse=True)).head(20)
    #print(total_actor_count)
    names = total_company_count.index
    count = total_company_count.values
    
    plt.barh(names,count)
    plt.title("Frequent production companies over the years")
    plt.xlabel('Number Of Movies')
    plt.ylabel("Priduction company name")
    plt.show()

    return None 

def most_common_country():
    ''' Production company with maximum releases over the years'''
    
    total_country_count = utils.unqiues_from_multiples(df['production_countries'])
    total_country_count = pd.Series(total_country_count, index = sorted(total_country_count, key=total_country_count.get, reverse=True)).head(20)
    #print(total_actor_count)
    names = total_country_count.index
    count = total_country_count.values
    
    plt.barh(names,count)
    plt.title("Frequent production companies over the years")
    plt.xlabel('Number Of Movies')
    plt.ylabel("Priduction company name")
    plt.show()
    
    return None

# actor with max releases over the year
most_common_actor()

# production company with max releases over the year
most_common_company()

# counties with max releases over the years
most_common_country()