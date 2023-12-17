#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

import os
pd.set_option('display.max_rows', 10)


# In[3]:


data_path = os.path.join('Data','input.txt')
data = pd.read_table(data_path)
data = data.T.reset_index().T.reset_index(drop = True)
data.rename(columns={0:'inputs'},inplace = True)
data


# In[33]:


a = np.array([list(x) for x in data['inputs']])


# In[55]:


a.shape


# In[86]:


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


# In[87]:


insert_count = 0
for i in rows_with_no_galaxy:
    a = np.insert(a, [i+insert_count], [['.']], axis = 0)
    insert_count += 1
insert_count = 0
for j in columns_with_no_galaxy:
    a = np.insert(a, [j+insert_count], [['.']], axis = 1)
    insert_count += 1


# In[88]:


no_of_galaxys = 0
galaxy_indices = []
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if a[i,j] == '#':
            no_of_galaxys += 1
            a[i,j] = int(no_of_galaxys)
            galaxy_indices.append([i,j])
no_of_galaxys


# In[68]:


no_of_galaxy_pairs = int(no_of_galaxys*(no_of_galaxys+1)/2)
no_of_galaxy_pairs


# In[ ]:





# In[ ]:




