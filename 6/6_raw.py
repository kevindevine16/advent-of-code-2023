#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import os
pd.set_option('display.max_rows', 10)


# In[2]:


def GetNumbers(string_of_nums):
    yy = string_of_nums[0].split(' ')
    b = False
    while b == False:
        if '' in yy:
            yy.remove('')
        else:
            b = True
    return yy


def CheckIfMyNumnbersWon(list_of_winning_numbers, list_of_my_numbers):
    list_of_my_winning_numbers = []
    for number in list_of_my_numbers:
        if number in list_of_winning_numbers:
            list_of_my_winning_numbers.append(int(number))
        
    return list_of_my_winning_numbers


# In[3]:


data_path = os.path.join('Data','input.txt')
data = pd.read_table(data_path)
data = data.T.reset_index().T.reset_index(drop = True)
data.rename(columns={0:'inputs'},inplace = True)
data['game_number'] = data['inputs'].apply(lambda input: int(input.split(': ')[0].split(' ')[-1]))
data['winning_Numbers'] = data['inputs'].apply(lambda input: input.split(': ')[1].split('| ')[0].split(', '))
data['my_Numbers'] = data['inputs'].apply(lambda input: input.split(': ')[1].split('| ')[1].split(', '))
data['list_of_winning_numbers'] =  data['winning_Numbers'].apply(lambda input: GetNumbers(input))
data['list_of_my_numbers'] =  data['my_Numbers'].apply(lambda input: GetNumbers(input))
data['list_of_my_winning_numbers'] = data.apply(lambda df: CheckIfMyNumnbersWon(df['list_of_winning_numbers'], df['list_of_my_numbers']), axis=1)
data['points_per_card'] = data['list_of_my_winning_numbers'].apply(lambda li: 2**(len(li)-1) if len(li) > 0 else 0)
data['count_of_my_winning_numbers'] = data['list_of_my_winning_numbers'].apply(lambda li: len(li))
data['number_of_originals'] = 1
data['number_of_copies'] = 0
data


# In[4]:


number_of_copies_dic = {}
for i in range(len(data)):
    number_of_copies_dic[i] = 0
for i in range(len(data)):
    copy_length = data['count_of_my_winning_numbers'].iloc[i]
    if (copy_length > 0) :
        for j in range(i+1,i+copy_length+1):
            if j <= len(data):
                number_of_copies_dic[j] += 1 + number_of_copies_dic[i]

    pass
number_of_copies_dic


# In[5]:


count = 0
for i in range(len(data)):
    count += number_of_copies_dic[i]
count+len(data)


# In[6]:


def CheckIfMyNumnbersWon(list_of_winning_numbers, list_of_my_numbers):
    list_of_my_winning_numbers = []
    for number in list_of_my_numbers:
        if number in list_of_winning_numbers:
            list_of_my_winning_numbers.append(int(number))
        
    return list_of_my_winning_numbers


# In[ ]:





# In[7]:


nums = []
for yy in data['winning_Numbers'].iloc[0][0].split('  '):
    print(yy)
    nums.append(yy.split(' '))

nums


# In[8]:


flat_list = [item for sublist in nums for item in sublist]
flat_list


# In[9]:


import sys
sys.path.append(os.pardir)
from src.HelperFunctions import convert_to_py

convert_to_py('4')

