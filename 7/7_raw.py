#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import os
pd.set_option('display.max_rows', 10)


# In[2]:


def GetHandType(hand:str)->list:
    handType = []
    for character in hand:
        handType.append(hand.count(character))
        hand.replace(character,'')
    handType.sort()
    return handType


# In[3]:


def GetHandTypeRank(HandType:list)->int:
    AllTypes = {tuple([5,5,5,5,5]):7,tuple([1,4,4,4,4]):6,tuple([2,2,3,3,3]):5,tuple([1,1,3,3,3]):4,tuple([1,2,2,2,2]):3,
                tuple([1,1,1,2,2]):2,tuple([1,1,1,1,1]):1}
    HandTypeRank = AllTypes[tuple(HandType)]
    return HandTypeRank


# In[4]:


def GetIndexRank(hand:str,
                 index:int)->int:
    card = hand[index]
    ranks = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}
    rank = ranks[card]
    return rank


# In[5]:


data_path = os.path.join('Data','input.txt')
data = pd.read_table(data_path)
data = data.T.reset_index().T.reset_index(drop = True)
data.rename(columns={0:'inputs'},inplace = True)
data['hands'] = data['inputs'].apply(lambda inputs: inputs.split(' ')[0])
data['bids'] = data['inputs'].apply(lambda inputs: int(inputs.split(' ')[1]))
data['handTypes'] = data['hands'].apply(lambda hand: GetHandType(hand))
data['handTypeRanks'] = data['handTypes'].apply(lambda hand: GetHandTypeRank(hand))
for i in range(5):
    data['rank_index'+str(i)] = data['hands'].apply(lambda hand: GetIndexRank(hand,i))
data.sort_values(['handTypeRanks', 'rank_index0','rank_index1','rank_index2','rank_index3','rank_index4'], ascending = True, inplace = True)
data.reset_index(inplace=True)
data['rank'] = data.index+1
data['winnings'] = data['bids']*data['rank']
data


# In[6]:


data['winnings'].sum()


# In[7]:


def GetIndexRank_2(hand:str,
                   index:int)->int:
    card = hand[index]
    ranks = {'J':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'Q':11,'K':12,'A':13}
    rank = ranks[card]
    return rank


# In[8]:


def JokerWild(hand:str)->int:
    HandType = GetHandType(hand)
    HandTypeRank = int(GetHandTypeRank(HandType))
    if 'J' in hand:
        for character in ['2','3','4','5','6','7','8','9','T','Q','K','A']:
            newHand = hand.replace('J',character)
            NewHandType = GetHandType(newHand)
            NewHandTypeRank = int(GetHandTypeRank(NewHandType))
            if NewHandTypeRank > HandTypeRank:
                HandTypeRank = NewHandTypeRank
    return HandTypeRank


# In[9]:


data_path = os.path.join('Data','input.txt')
data = pd.read_table(data_path)
data = data.T.reset_index().T.reset_index(drop = True)
data.rename(columns={0:'inputs'},inplace = True)
data['hands'] = data['inputs'].apply(lambda inputs: inputs.split(' ')[0])
data['bids'] = data['inputs'].apply(lambda inputs: int(inputs.split(' ')[1]))
data['newHandTypeRanks'] = data['hands'].apply(lambda hand: JokerWild(hand))
for i in range(5):
    data['rank_index'+str(i)] = data['hands'].apply(lambda hand: GetIndexRank_2(hand,i))
data.sort_values(['newHandTypeRanks', 'rank_index0','rank_index1','rank_index2','rank_index3','rank_index4'], ascending = True, inplace = True)
data.reset_index(inplace=True)
data['rank'] = data.index+1
data['winnings'] = data['bids']*data['rank']
data


# In[10]:


data['winnings'].sum()


# In[11]:


import sys
sys.path.append(os.pardir)
from src.HelperFunctions import convert_to_py

convert_to_py('7')

