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


times = data.iloc[0,0].split('Time: ')[1]
times =  times.split(' ')
while '' in times:
    times.remove('')

times = [ int(time) for time in times ]
times


# In[4]:


distances = data.iloc[1,0].split('Distance: ')[1]
distances = distances.split(' ')
while '' in distances:
    distances.remove('')
distances = [ int(distance) for distance in distances ]
distances


# In[5]:


num_of_ways_race = []
for i in range(len(times)):    
    num_of_ways = 0
    for j in range(1,times[i]):
        if (times[i]-j)*j > distances[i]:
            num_of_ways+=1
        pass
    num_of_ways_race.append(num_of_ways)
num_of_ways_race
product = 1
for number in num_of_ways_race:
    product *= number
product


# In[6]:


times = data.iloc[0,0].split('Time: ')[1]
times =  times.split(' ')
while '' in times:
    times.remove('')
times
time = ''
for t in times:
    time += t
time = int(time)


# In[7]:


distances = data.iloc[1,0].split('Distance: ')[1]
distances =  distances.split(' ')
while '' in distances:
    distances.remove('')
distances
distance = ''
for d in distances:
    distance += d
distance = int(distance)


# In[8]:


num_of_ways = 0
for j in range(1,time):
    if (time-j)*j > distance:
        num_of_ways+=1
    pass
num_of_ways


# In[10]:


import sys
sys.path.append(os.pardir)
from src.HelperFunctions import convert_to_py

convert_to_py('6')

