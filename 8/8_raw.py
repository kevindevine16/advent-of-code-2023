#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import os
pd.set_option('display.max_rows', 10)


# In[2]:


def GetLHS(string):
    string = string.split(' = (')[0].replace(')','')
    return string


# In[3]:


def GetRHS(string):
    string = string.split('(')[1].replace(')','')
    return string.split(', ')


# In[4]:


data_path = os.path.join('Data','input.txt')
data = pd.read_table(data_path)
data = data.T.reset_index().T.reset_index(drop = True)
data.rename(columns={0:'inputs'},inplace = True)
LR_key = data.iloc[0,0]
data = data.tail(-1)
data['LHS'] = data['inputs'].apply(lambda input: GetLHS(input))
data['RHS'] = data['inputs'].apply(lambda input: GetRHS(input))
data


# In[5]:


mapDic = {}
for i in range(len(data)):
    mapDic[data['LHS'].iloc[i]] = data['RHS'].iloc[i]


# In[6]:


LR_key = LR_key.replace('L','0')
LR_key = LR_key.replace('R','1')


# In[7]:


numberOfSteps = 0
i = 0
key = 'AAA'
while key != 'ZZZ':
    key = mapDic[key][int(LR_key[i])]
    numberOfSteps += 1
    i+=1
    if i == len(LR_key):
        i = 0
numberOfSteps


# In[8]:


startSet = []
for i in range(len(data)):
    if data['LHS'].iloc[i][-1] == 'A':
        startSet.append(data['LHS'].iloc[i])
startSet


# In[9]:


StepsStore = []
i = 0
keys = startSet
for key in keys:
    numberOfSteps = 0
    checkBool = False
    while not checkBool:
        key = mapDic[key][int(LR_key[i])]
        numberOfSteps += 1
        i+=1
        if i == len(LR_key):
            i = 0
        #print(keys)
        checkBool = key[-1] == 'Z'
    StepsStore.append(numberOfSteps)
StepsStore


# In[10]:


from math import gcd
lcm = 1
for i in StepsStore:
    lcm = lcm*i//gcd(lcm, i)
lcm


# In[11]:


import sys
sys.path.append(os.pardir)
from src.HelperFunctions import convert_to_py

convert_to_py('8')

