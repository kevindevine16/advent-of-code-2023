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


# In[4]:


a = np.array([list(x) for x in data['inputs']])
a.shape


# In[5]:


a


# In[62]:


a = np.array([list(x) for x in data['inputs']])
def FindStart(a):
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
    #a[a == 'S'] = 0
    #print(Second_Indices)
    #Second_Indices = [np.array(element) for element in Second_Indices]
    return Start_Index[0], Second_Indices, Second_Elements

Start_Index, Second_Indices, Second_Elements = FindStart(a)
Second_Indices = FindStart(a)[1]
Start_Index
Second_Indices
#Second_Elements


# In[7]:


Start_Index + np.array([1,0])


# In[64]:


Second_Indices


# In[65]:


Second_Elements


# In[94]:


def FindDistances(Start_Index,
                  Second_Indices,
                  Second_Elements, a):
    
    first_previous_i = Start_Index[0]
    first_previous_j = Start_Index[1]
    second_previous_i = Start_Index[0]
    second_previous_j = Start_Index[1]
    first_next_i = Second_Indices[0][0]
    first_next_j = Second_Indices[0][1]
    first_next_element = Second_Elements[0]
    second_next_i = Second_Indices[1][0]
    second_next_j = Second_Indices[1][1]
    second_next_element = Second_Elements[1]
    distance = 0
    
    while (~(first_next_i != second_next_i) and ~(first_next_j != second_next_j)) or ():
    # for _ in range(20):
        print(first_next_element)
        #print(a[first_next_i, first_next_j])
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
                #print('SHouldnt print',first_next_i,first_previous_i)
                first_previous_i = first_next_i
                first_previous_j = first_next_j
                first_next_i -= 1
            #print(first_previous_i,first_previous_j)
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
        elif (first_next_element == 'S'):
            pass
        else:
            raise Exception
        
        #print(second_next_element)
        # print(second_next_i,second_next_j)
        # print(second_previous_i,second_previous_j)
        if (second_next_element == 'F'): 
            
            if (second_next_j < second_previous_j):
                second_previous_i = second_next_i
                second_previous_j = second_next_j
                second_next_i +=1
            else: 
                second_previous_i = second_next_i
                second_previous_j = second_next_j
                second_next_j += 1
            
            second_next_element = a[second_next_i,second_next_j]
        elif (second_next_element == '|'):
            if (second_next_i < second_previous_i):
                second_previous_i = second_next_i
                second_previous_j = second_next_j
                second_next_i -= 1
            else: 
                second_previous_i = second_next_i
                second_previous_j = second_next_j
                second_next_i += 1
            second_next_element = a[second_next_i,second_next_j]
        elif (second_next_element == '-'):
            if (second_next_j < second_previous_j):
                second_previous_i = second_next_i
                second_previous_j = second_next_j
                second_next_j -= 1
            else: 
                second_previous_i = second_next_i
                second_previous_j = second_next_j
                second_next_j += 1
            second_next_element = a[second_next_i,second_next_j]
        elif (second_next_element == 'L'):
            if (second_next_i > second_previous_i):
                second_previous_i = second_next_i
                second_previous_j = second_next_j
                second_next_j += 1
            else:
                #print('SHouldnt print',first_next_i,first_previous_i)
                second_previous_i = second_next_i
                second_previous_j = second_next_j
                second_next_i -= 1
            #print(first_previous_i,first_previous_j)
            second_next_element = a[second_next_i,second_next_j]
        elif (second_next_element == '7'):
            if (second_next_i < second_previous_i):
                second_previous_i = second_next_i 
                second_previous_j = second_next_j
                #print(second_previous_i,second_previous_j)
                second_next_j -= 1
                #print(second_next_j)
            else: 
                second_previous_i = second_next_i
                second_previous_j = second_next_j
                #print(second_previous_i)
                second_next_i += 1
            second_next_element = a[second_next_i,second_next_j]
        elif (second_next_element == 'J'):
            if (second_next_i > second_previous_i):
                second_previous_i = second_next_i
                second_previous_j = second_next_j
                second_next_j -= 1
            else: 
                second_previous_i = second_next_i
                second_previous_j = second_next_j
                second_next_i -= 1
            second_next_element = a[second_next_i,second_next_j]
        else:
            pass
            #raise Exception
        distance+=1

        pass

    return distance


# In[95]:


FindDistances(Start_Index,
                  Second_Indices,
                  Second_Elements, a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import sys
sys.path.append(os.pardir)
from src.HelperFunctions import convert_to_py

convert_to_py('10')

