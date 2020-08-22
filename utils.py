# -*- coding: utf-8 -*-
"""
@author: Anu
"""


def highest_and_lowest_entity(datacol):
    '''Return index based on highest and
    lowest value of passed particular column resp'''
 
    minimim = datacol.idxmin()
    maximum = datacol.idxmax()
    
    return (maximum,minimim)

def unqiues_from_multiples(datacol):
    '''Return dict of unqiue values from datacols with 
    multiple values separated by ','''

    unique_count = dict({})
    for column in datacol:
        column = str(column)
        for genre in column.split(','):
            genre = genre.strip()
            if genre in unique_count:
                unique_count[genre] = unique_count[genre] + 1
            else:
                unique_count[genre] = 1
    return unique_count


def no_values_in_range(datacol, start, end):
    '''Return number of values from datacols in given range
    start inclusive and end exclusive'''

    import numpy as np

    return len(np.array([i for i in datacol if (i >= start and i < end)]))


def sort_dict_on_sortable_values(datadic):
    '''Return number the dictionary sorted based on values'''

    sort_dict = dict({})
    parsing = sorted(datadic, key=datadic.get, reverse=True)
    for key in parsing:
        sort_dict[key] = datadic[key]
    return sort_dict

def group_creation(datacol):
    '''Return tuple of (list of group_name,list of group_data) of datacol'''

    group_data = [datacol.min(), datacol.describe()[4], datacol.describe()[5], datacol.describe()[6],datacol.max()]
    group_name = ['Low', 'Moderate','Moderately High','High']
    return (group_name, group_data)
    