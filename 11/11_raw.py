#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import os
pd.set_option('display.max_rows', 10)


# In[2]:


data_path = os.path.join('Data','input.txt')
data = pd.read_table(data_path)
data = data.T.reset_index().T.reset_index(drop = True)
data.rename(columns={0:'inputs'},inplace = True)
data


# In[3]:


a = np.array([list(x) for x in data['inputs']], dtype='U25')
def RowsAndColumnsNoGalaxy(a:np.ndarray)->tuple:
    rows_with_no_galaxy = []
    for i in range(a.shape[0]):
        if '#' not in a[i,:]:
            rows_with_no_galaxy.append(i)
    columns_with_no_galaxy = []
    for j in range(a.shape[1]):
        if '#' not in a[:,j]:
            columns_with_no_galaxy.append(j)
    return rows_with_no_galaxy, columns_with_no_galaxy
rows_with_no_galaxy, columns_with_no_galaxy = RowsAndColumnsNoGalaxy(a)


# In[4]:


insert_count = 0
row_insert_index = []
for i in rows_with_no_galaxy:
    row_insert_index.append(i+insert_count)

insert_count = 0
column_insert_index = []
for j in columns_with_no_galaxy:
    column_insert_index.append(j+insert_count)


# In[5]:


no_of_galaxys = 0
galaxy_indices = []
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if a[i,j] == '#':
            no_of_galaxys += 1
            a[i,j] = int(no_of_galaxys)
            galaxy_indices.append([i,j])
no_of_galaxys


# In[6]:


no_of_galaxy_pairs = int(no_of_galaxys*(no_of_galaxys+1)/2)-no_of_galaxys
no_of_galaxy_pairs


# In[7]:


galaxy_pairs = []
counter = 0
for k in range(len(galaxy_indices)):
    for m in range(k+1,len(galaxy_indices)):
        galaxy_pairs.append([galaxy_indices[k],galaxy_indices[m]])
        counter+=1
        pass
counter


# In[8]:


distance_sums = 0
for i in range(len(galaxy_pairs)):
    for row_index in row_insert_index:
        if row_index in range(galaxy_pairs[i][0][0],galaxy_pairs[i][1][0]) or row_index in range(galaxy_pairs[i][1][0],galaxy_pairs[i][0][0]):
            distance_sums += 2-1
    for column_index in column_insert_index:
        if column_index in range(galaxy_pairs[i][0][1],galaxy_pairs[i][1][1]) or column_index in range(galaxy_pairs[i][1][1],galaxy_pairs[i][0][1]):
            distance_sums += 2-1
    distance_sums += abs(galaxy_pairs[i][0][0]-galaxy_pairs[i][1][0])+abs(galaxy_pairs[i][0][1]-galaxy_pairs[i][1][1])


# In[9]:


distance_sums


# In[10]:


distance_sums = 0
for i in range(len(galaxy_pairs)):
    for row_index in row_insert_index:
        if row_index in range(galaxy_pairs[i][0][0],galaxy_pairs[i][1][0]) or row_index in range(galaxy_pairs[i][1][0],galaxy_pairs[i][0][0]):
            distance_sums += int(1e6)-1
    for column_index in column_insert_index:
        if column_index in range(galaxy_pairs[i][0][1],galaxy_pairs[i][1][1]) or column_index in range(galaxy_pairs[i][1][1],galaxy_pairs[i][0][1]):
            distance_sums += int(1e6)-1
    distance_sums += abs(galaxy_pairs[i][0][0]-galaxy_pairs[i][1][0])+abs(galaxy_pairs[i][0][1]-galaxy_pairs[i][1][1])


# In[11]:


distance_sums


# In[12]:


import sys
sys.path.append(os.pardir)
from src.HelperFunctions import convert_to_py

convert_to_py('11')

