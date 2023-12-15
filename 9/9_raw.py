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


# In[3]:


def StringsToListOfInts(inputs):
    strings = inputs.split(' ')
    integers = [int(integer) for integer in strings]
    return integers


# In[4]:


data['integers'] = data['inputs'].apply(lambda inputs: StringsToListOfInts(inputs))
data


# In[5]:


def GetPrediction(listOfInts:list)->int:
    steps = 0
    dic = {}
    while not all(integer == 0 for integer in listOfInts):
        dic[steps] = listOfInts[-1]
        listOfInts = np.diff(listOfInts)
        steps += 1
    prediction = 0
    for i in range(steps):
        prediction = prediction + dic[steps-1-i]
        pass
    return prediction


# In[6]:


data['predictions'] = data['integers'].apply(lambda integers: GetPrediction(integers))
data


# In[7]:


data['predictions'].sum()


# In[8]:


tester = data['integers'].iloc[2]
def GetPrediction_2(listOfInts:list)->int:
    steps = 0
    dic = {}
    while not all(integer == 0 for integer in listOfInts):
        dic[steps] = listOfInts[0]
        listOfInts = np.diff(listOfInts)
        steps += 1
    prediction = 0
    for i in range(steps):
        prediction = - prediction + dic[steps-1-i]
        pass
    return prediction
GetPrediction_2(tester)


# In[9]:


data['predictions_2'] = data['integers'].apply(lambda integers: GetPrediction_2(integers))
data


# In[10]:


data['predictions_2'].sum()


# In[11]:


import sys
sys.path.append(os.pardir)
from src.HelperFunctions import convert_to_py

convert_to_py('9')

