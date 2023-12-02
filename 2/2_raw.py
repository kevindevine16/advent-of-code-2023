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
data['game_number'] = data['inputs'].apply(lambda input: int(input.split(':')[0].split(' ')[1]))
data['draws'] = data['inputs'].apply(lambda input: input.split(':')[1])
data['draws_split'] = data['draws'].apply(lambda draw: draw.split(';'))


# In[3]:


def getReds(draw_split:str)->list:
    numOfReds = []
    for i in range(len(draw_split)):
        if 'red' in draw_split[i]:
            color_split = draw_split[i].split(',')
            for cs in color_split:
                if 'red' in cs:
                    numOfReds.append(int(cs.strip().split(' ')[0]))
        else:
            numOfReds.append(0)
            
    return numOfReds

def getBlues(draw_split:str)->list:
    numOfBlues = []
    for i in range(len(draw_split)):
        if 'blue' in draw_split[i]:
            color_split = draw_split[i].split(',')
            for cs in color_split:
                if 'blue' in cs:
                    numOfBlues.append(int(cs.strip().split(' ')[0]))
        else:
            numOfBlues.append(0)
            
    return numOfBlues

def getGreens(draw_split:str)->list:
    numOfGreens = []
    for i in range(len(draw_split)):
        if 'green' in draw_split[i]:
            color_split = draw_split[i].split(',')
            for cs in color_split:
                if 'green' in cs:
                    numOfGreens.append(int(cs.strip().split(' ')[0]))
        else:
            numOfGreens.append(0)
            
    return numOfGreens



# In[4]:


data['Reds_list'] = data['draws_split'].apply(lambda draws: getReds(draws))
data['Blues_list'] = data['draws_split'].apply(lambda draws: getBlues(draws))
data['Greens_list'] = data['draws_split'].apply(lambda draws: getGreens(draws))


# In[5]:


def checkPossible(my_list:list, 
                  my_max:int)->bool:
    for cubes in my_list:
        if cubes > my_max:
            return False
        else:
            pass
    return True

data['Reds_possible'] = data['Reds_list'].apply(lambda my_list: checkPossible(my_list = my_list, my_max = 12))
data['Greens_possible'] = data['Greens_list'].apply(lambda my_list: checkPossible(my_list = my_list, my_max = 13))
data['Blues_possible'] = data['Blues_list'].apply(lambda my_list: checkPossible(my_list = my_list, my_max = 14))


# In[6]:


data_possible = data[['game_number','Reds_list','Greens_list','Blues_list','Reds_possible','Greens_possible','Blues_possible']][(data['Reds_possible']) & (data['Greens_possible']) & (data['Blues_possible'])]
data_possible['game_number'].sum()


# In[7]:


data['minimum_reds_needed'] = data['Reds_list'].apply(lambda cubes: np.max(cubes))
data['minimum_greens_needed'] = data['Greens_list'].apply(lambda cubes: np.max(cubes))
data['minimum_blues_needed'] = data['Blues_list'].apply(lambda cubes: np.max(cubes))
data['power'] = data['minimum_reds_needed']*data['minimum_greens_needed']*data['minimum_blues_needed']


# In[8]:


data['power'].sum()

