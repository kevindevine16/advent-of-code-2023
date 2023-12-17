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


a = np.array([list(x) for x in data['inputs']])
def FindStart(a: np.ndarray) -> tuple:
    Start_Index = []
    Second_Indices = []
    Second_Elements = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 'S':
                Start_Index.append([i,j])
    i = Start_Index[0][0]
    j = Start_Index[0][1]
    if (a[i][j-1] == 'L') or (a[i][j-1] == 'F') or (a[i][j-1] == '-'):
        Second_Indices.append([i,j-1])
        Second_Elements.append(a[i,j-1])
    if (a[i][j+1] == 'J') or (a[i][j+1] == '7') or (a[i][j+1] == '-'):
        Second_Indices.append([i,j+1])
        Second_Elements.append(a[i,j+1])
    if (a[i+1][j] == 'L') or (a[i+1][j] == 'J') or (a[i+1][j] == '|'):
        Second_Indices.append([i+1,j])
        Second_Elements.append(a[i+1,j])
    if (a[i-1][j] == '7') or (a[i-1][j] == 'F') or (a[i-1][j] == '|'):
        Second_Indices.append([i-1,j])
        Second_Elements.append(a[i-1,j])
    
    return Start_Index[0], Second_Indices, Second_Elements

Start_Index, Second_Indices, Second_Elements = FindStart(a)


# In[4]:


def FindPipeIndices(Start_Index:list,
                  Second_Indices:list,
                  Second_Elements:list, 
                  a:np.ndarray)->list:
    first_previous_i = Start_Index[0]
    first_previous_j = Start_Index[1]
    first_next_i = Second_Indices[0][0]
    first_next_j = Second_Indices[0][1]
    pipe_indices = [[first_previous_i,first_previous_j],[first_next_i, first_next_j]]
    first_next_element = Second_Elements[0]
    while a[first_next_i][first_next_j] != 'S':
        if (first_next_element == 'F'): 
            if (first_next_j < first_previous_j):
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_i +=1
            else: 
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_j += 1
            first_next_element = a[first_next_i,first_next_j]
        elif (first_next_element == '|'):
            if (first_next_i < first_previous_i):
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_i -= 1
            else: 
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_i += 1
            first_next_element = a[first_next_i,first_next_j]
        elif (first_next_element == '-'):
            if (first_next_j < first_previous_j):
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_j -= 1
            else: 
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_j += 1
            first_next_element = a[first_next_i,first_next_j]
        elif (first_next_element == 'L'):
            if (first_next_i > first_previous_i):
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_j += 1
            else:
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_i -= 1
            first_next_element = a[first_next_i,first_next_j]
        elif (first_next_element == '7'):
            if (first_next_i < first_previous_i):
                first_previous_i = first_next_i
                first_previous_j = first_next_j 
                first_next_j -= 1
            else: 
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_i += 1
            first_next_element = a[first_next_i,first_next_j]
        elif (first_next_element == 'J'):
            if (first_next_i > first_previous_i):
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_j -= 1
            else: 
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_i -= 1
            first_next_element = a[first_next_i,first_next_j]
        elif(first_next_element == 'S'):
            pass
        else:
            raise Exception

        pipe_indices.append([first_next_i, first_next_j])

        pass

    return pipe_indices


# In[5]:


pipe_indices = FindPipeIndices(Start_Index,
                             Second_Indices,
                             Second_Elements, 
                             a)
distance_from_animal = int(len(pipe_indices[0:-1])/2)
distance_from_animal


# [Shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula) to get area enclosed by pipe.

# In[6]:


def GetArea(pipe_indices:list)->int:
    Area = 0
    for k in range(len(pipe_indices[0:-1])):
        Area += 0.5*np.linalg.det(np.array([pipe_indices[k],pipe_indices[k+1]]).transpose())
    return int(abs(Area))


# In[7]:


Area = GetArea(pipe_indices)


# [Pick's theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem) to find number of interior points.

# In[8]:


interior_points = Area - distance_from_animal - 0 + 1
interior_points


# In[9]:


import sys
sys.path.append(os.pardir)
from src.HelperFunctions import convert_to_py

convert_to_py('10')

