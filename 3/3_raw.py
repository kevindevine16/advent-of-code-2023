#!/usr/bin/env python
# coding: utf-8

# In[729]:


import numpy as np
import pandas as pd

import os
pd.set_option('display.max_rows', 10)


# In[730]:


data_path = os.path.join('Data','input_part2_2.txt')
data = pd.read_table(data_path)
data = data.T.reset_index().T.reset_index(drop = True)
data.rename(columns={0:'inputs'},inplace = True)
data


# In[731]:


arr = np.array([*data.inputs])
arr


# In[732]:


list(arr[0])
a = np.array([list(x) for x in data['inputs']])
a.shape


# In[733]:


for i in range(1,len(a)-1):
    j = 0
    while j < len(a):
        k = 1
        if a[i,-1-j].isdigit():
            digit = True 
            while digit:
                #print(i,j,k)
                if not a[i,-1-j-k].isdigit():
                    lenNum = k
                    digit = False
                else:
                    k  +=1
                    if k+j == 140:
                        digit = False
            num = 0
            for kk in range(k):
                num += int(a[i,-1-j-kk])*(10**kk)
            print(num)
            j = j+k
        #for jj in []
        j +=1
        pass


# In[734]:


def getNumber(a):
    VaildNumbers = []

    j = 0
    while j < len(a):
        k = 1
        if a[0,-1-j].isdigit():
            digit = True 
            while digit:
                #print(i,j,k)
                if not a[0,-1-j-k].isdigit():
                    lenNum = k
                    digit = False
                else:
                    k  +=1
                    if k+j == 140:
                        digit = False
            num = 0
            for kk in range(k):
                num += int(a[0,-1-j-kk])*(10**kk)
            #print(num)

            if j == 0:
                Valid = False
                kkk = 0
                while kkk <k+1 :
                    if (not a[1,-1-kkk].isdigit()) and (a[1,-1-kkk] != '.') :
                        Valid = True
                        kkk = k+1
                    kkk += 1
                if (not a[0,-1-k].isdigit()) and (a[0,-1-k] != '.') :
                        Valid = True

                if Valid:
                    numValid = num
                    VaildNumbers.append(numValid)
                
            elif j+k == 140:
                Valid = False
                kkk = 0
                while kkk < (k+1) :
                    if (not a[1,kkk].isdigit()) and (a[1,kkk] != '.') :
                        Valid = True
                        kkk = k+1
                    kkk += 1
                if (not a[0,k+1].isdigit()) and (a[0,k+1] != '.') :
                        Valid = True

                if Valid:
                    numValid = num
                    VaildNumbers.append(numValid)
            else:
                Valid = False
                kkk = -1
                while kkk < (k+1) :
                    # print(-j-kkk)
                    if (not a[-1,-1-j-kkk].isdigit()) and (a[-1,-1-j-kkk] != '.') :
                        Valid = True
                        kkk = k
                    # print(j+k)
                    # print(j)
                    # print(kkk)
                    # print(num)
                    if (not a[1,-1-j-kkk].isdigit()) and (a[1,-1-j-kkk] != '.') :
                        Valid = True
                        kkk = k
                    kkk += 1
                if (not a[0,-1-k-j].isdigit()) and (a[0,-1-k-j] != '.') :
                        Valid = True
                if (not a[0,-j].isdigit()) and (a[0,-j] != '.') :
                        Valid = True
                if Valid:
                    numValid = num
                    VaildNumbers.append(numValid)                    
            j = j+k
        j +=1
        pass


    for i in range(1,len(a)-1):
        j = 0
        while j < len(a):
            k = 1
            if a[i,-1-j].isdigit():
                digit = True 
                while digit:
                    #print(i,j,k)
                    if not a[i,-1-j-k].isdigit():
                        lenNum = k
                        digit = False
                    else:
                        k  +=1
                        if k+j == 140:
                            digit = False
                num = 0
                for kk in range(k):
                    num += int(a[i,-1-j-kk])*(10**kk)

                if j == 0:
                    Valid = False
                    kkk = 0
                    while kkk <k+1 :
                        if (not a[i-1,-1-kkk].isdigit()) and (a[i-1,-1-kkk] != '.') :
                            Valid = True
                            kkk = k+1
                        if (not a[i+1,-1-kkk].isdigit()) and (a[i+1,-1-kkk] != '.') :
                            Valid = True
                            kkk = k+1
                        kkk += 1
                    if (not a[i,-1-k].isdigit()) and (a[i,-1-k] != '.') :
                            Valid = True

                    if Valid:
                        numValid = num
                        VaildNumbers.append(numValid)
                    
                elif j+k == 140:
                    Valid = False
                    kkk = 0
                    while kkk < (k+1) :
                        if (not a[i-1,kkk].isdigit()) and (a[i-1,kkk] != '.') :
                            Valid = True
                            kkk = k+1
                        if (not a[i+1,kkk].isdigit()) and (a[i+1,kkk] != '.') :
                            Valid = True
                            kkk = k+1
                        kkk += 1
                    if (not a[i,k+1].isdigit()) and (a[i,k+1] != '.') :
                            Valid = True

                    if Valid:
                        numValid = num
                        VaildNumbers.append(numValid)
                else:
                    Valid = False
                    kkk = -1
                    while kkk < (k+1) :
                        # print(-j-kkk)
                        if (not a[i-1,-1-j-kkk].isdigit()) and (a[i-1,-1-j-kkk] != '.') :
                            Valid = True
                            kkk = k
                        if (not a[i+1,-1-j-kkk].isdigit()) and (a[i+1,-1-j-kkk] != '.') :
                            Valid = True
                            kkk = k
                        kkk += 1
                    if (not a[i,-1-k-j].isdigit()) and (a[i,-1-k-j] != '.') :
                            Valid = True
                    if (not a[i,-j].isdigit()) and (a[i,-j] != '.') :
                            Valid = True
                    if Valid:
                        numValid = num
                        VaildNumbers.append(numValid)                    
                j = j+k
            j +=1
            pass

    j = 0
    while j < len(a):
        k = 1
        if a[(len(a)-1),-1-j].isdigit():
            digit = True 
            while digit:
                #print(i,j,k)
                if not a[(len(a)-1),-1-j-k].isdigit():
                    lenNum = k
                    digit = False
                else:
                    k  +=1
                    if k+j == 140:
                        digit = False
            num = 0
            for kk in range(k):
                num += int(a[(len(a)-1),-1-j-kk])*(10**kk)
            #print(num)

            if j == 0:
                Valid = False
                kkk = 0
                while kkk <k+1 :
                    if (not a[(len(a)-1)-1,-1-kkk].isdigit()) and (a[(len(a)-1)-1,-1-kkk] != '.') :
                        Valid = True
                        kkk = k+1
                    kkk += 1
                if (not a[(len(a)-1),-1-k].isdigit()) and (a[(len(a)-1),-1-k] != '.') :
                        Valid = True

                if Valid:
                    numValid = num
                    VaildNumbers.append(numValid)
                
            elif j+k == 140:
                Valid = False
                kkk = 0
                while kkk < (k+1) :
                    if (not a[(len(a)-1)-1,kkk].isdigit()) and (a[(len(a)-1)-1,kkk] != '.') :
                        Valid = True
                        kkk = k+1
                    kkk += 1
                if (not a[(len(a)-1),k+1].isdigit()) and (a[(len(a)-1),k+1] != '.') :
                        Valid = True

                if Valid:
                    numValid = num
                    VaildNumbers.append(numValid)
            else:
                Valid = False
                kkk = -1
                while kkk < (k+1) :
                    # print(-j-kkk)
                    if (not a[(len(a)-1)-1,-1-j-kkk].isdigit()) and (a[(len(a)-1)-1,-1-j-kkk] != '.') :
                        Valid = True
                        kkk = k
                    # print(j+k)
                    # print(j)
                    # print(kkk)
                    # print(num)
                    kkk += 1
                if (not a[(len(a)-1),-1-k-j].isdigit()) and (a[(len(a)-1),-1-k-j] != '.') :
                        Valid = True
                if (not a[(len(a)-1),-j].isdigit()) and (a[(len(a)-1),-j] != '.') :
                        Valid = True
                if Valid:
                    numValid = num
                    VaildNumbers.append(numValid)                    
            j = j+k
        j +=1
        pass



    return VaildNumbers

Nums = getNumber(a)


# In[735]:


a[len(a)-1]


# In[736]:


np.sum(Nums)


# In[737]:


l = [1,2,3]
np.prod(l)


# In[738]:


a[1]


# In[739]:


a = np.array([list(x) for x in data['inputs']])
a.shape
a[1]


# In[740]:


def getNumbersOnly(row):
    nums = []
    start_indexes = []
    end_indexes = []
    num_lengths = []
    j = 0
    while j < len(row):
        k = 1
        if row[-1-j].isdigit():
            digit = True 
            while digit:
                #print(i,j,k)
                if not row[-1-j-k].isdigit():
                    lenNum = k
                    digit = False
                else:
                    k  +=1
                    if k+j == 140:
                        digit = False
            num = 0
            for kk in range(k):
                num += int(row[-1-j-kk])*(10**kk)
            nums.append(num)
            start_indexes.append(140-j-k)
            end_indexes.append(139-j)
            num_lengths.append(k)
            j = j+k
        j +=1    
    return nums, num_lengths, start_indexes, end_indexes
getNumbersOnly(a[3])


# In[741]:


nums_in_rows = []
nums_lengths = []
start_indeces_in_rows = []
end_indeces_in_rows = []
sets_of_adjacents = []
for i in range(len(a)):
    nums_in_row, num_lengths, start_indeces_in_row, end_indeces_in_row = getNumbersOnly(a[i])
    
    nums_in_rows.append(nums_in_row)
    nums_lengths.append(num_lengths)
    start_indeces_in_rows.append(start_indeces_in_row)
    end_indeces_in_rows.append(end_indeces_in_row)
    
    if i == 0:
        for j in range(len(nums_in_row)):
            set_of_adjacent = []

            if start_indeces_in_row[j] == 0:
                    # print(nums_in_row[j])
                    set_of_adjacent.append([i,end_indeces_in_row[j]+1,nums_in_row[j]])
                    # print([i,end_indeces_in_row[j]+1])
                    pass
            elif end_indeces_in_row[j] == 139:
                    set_of_adjacent.append([i,start_indeces_in_row[j]-1,nums_in_row[j]])
                    pass
            

            else:
                for ii in [i,i+1]:
                    set_of_adjacent.append([ii,start_indeces_in_row[j]-1,nums_in_row[j]])
                    set_of_adjacent.append([ii,end_indeces_in_row[j]+1,nums_in_row[j]])
                    if ii != i:
                        for kk in range(num_lengths[j]):
                            set_of_adjacent.append([ii,start_indeces_in_row[j]+kk,nums_in_row[j]])
                            pass
            sets_of_adjacents.append(set_of_adjacent)
   
    elif i == 139:

        for j in range(len(nums_in_row)):
            set_of_adjacent = []

            if start_indeces_in_row[j] == 0:
                
            
                # print(nums_in_row[j])
                set_of_adjacent.append([i,end_indeces_in_row[j]+1,nums_in_row[j]])
                # print([i,end_indeces_in_row[j]+1])
                pass
            elif end_indeces_in_row[j] == 139:
                    set_of_adjacent.append([i,start_indeces_in_row[j]-1,nums_in_row[j]])
                    pass

            else:
                for ii in [i-1,i]:
                    set_of_adjacent.append([ii,start_indeces_in_row[j]-1,nums_in_row[j]])
                    set_of_adjacent.append([ii,end_indeces_in_row[j]+1,nums_in_row[j]])
                    if ii != i:
                        for kk in range(num_lengths[j]):
                            set_of_adjacent.append([ii,start_indeces_in_row[j]+kk,nums_in_row[j]])
                            pass

            sets_of_adjacents.append(set_of_adjacent)

            pass
    else:
        for j in range(len(nums_in_row)):
            set_of_adjacent = []
            
            if start_indeces_in_row[j] == 0:
                # print(nums_in_row[j])
                set_of_adjacent.append([i,end_indeces_in_row[j]+1,nums_in_row[j]])
                # print([i,end_indeces_in_row[j]+1])
                pass

            elif end_indeces_in_row[j] == 139:
                set_of_adjacent.append([i,start_indeces_in_row[j]-1,nums_in_row[j]])
                pass

            else:
                for ii in [i-1,i,i+1]:
                    set_of_adjacent.append([ii,start_indeces_in_row[j]-1,nums_in_row[j]])
                    set_of_adjacent.append([ii,end_indeces_in_row[j]+1,nums_in_row[j]])
                    if ii != i:
                        for kk in range(num_lengths[j]):
                            set_of_adjacent.append([ii,start_indeces_in_row[j]+kk,nums_in_row[j]])
                            pass
            sets_of_adjacents.append(set_of_adjacent)


    
# start_indeces_in_rows[7]
sets_of_adjacents
print(nums_in_rows)
print(nums_lengths)
# end_indeces_in_rows
print(start_indeces_in_rows)
print(end_indeces_in_rows)
# len(sets_of_adjacents)
#print(len(nums_in_rows))


# In[742]:


def FindGears(a):
    num_gears = 0
    Gears_indices = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == '*':
                Gears_indices.append([i,j])
                num_gears += 1
    print(num_gears)
    return Gears_indices

Gears_Indices = FindGears(a)
len(Gears_Indices)


# In[743]:


# sets_of_adjacents


# In[744]:


gear_pairs = {}
gears_with_one_number = 0
gears_with_two_numbers = 0
product_pairs = []
product_pairs_products = []
for gear_index in Gears_Indices:
    gear_pairs[tuple(gear_index)] = [np.nan]
#for gear_index in Gears_Indices:
    for i in range(len(sets_of_adjacents)):
        for j in range(len(sets_of_adjacents[i])):
            if gear_index == sets_of_adjacents[i][j][0:2]:
                #print(gear_index)
                gear_pairs[tuple(gear_index)].append(sets_of_adjacents[i][j][2])
    if len(gear_pairs[tuple(gear_index)]) == 3:
        product_pairs.append([gear_pairs[tuple(gear_index)][1],gear_pairs[tuple(gear_index)][2]])
        product_pairs_products.append(gear_pairs[tuple(gear_index)][1]*gear_pairs[tuple(gear_index)][2])
        gears_with_two_numbers += 1

    if len(gear_pairs[tuple(gear_index)]) == 2:
        gears_with_one_number += 1
        #('hello')
gears_with_one_number
gears_with_two_numbers


# In[745]:


len(gear_pairs[tuple( [2, 27])])


# In[746]:


#gear_pairs[tuple([2, 27])].append(sets_of_adjacents[0][0][2])
#sets_of_adjacents[0][0][2]
#sets_of_adjacents[0][0][0:2]


# In[747]:


gear_pairs[tuple([2, 27])]


# In[748]:


gear_pairs


# In[749]:


product_pairs


# In[750]:


len(gear_pairs)


# In[751]:


len(Gears_Indices)


# In[752]:


ss = 0
for pairs in product_pairs:
    ss += pairs[0]*pairs[1]
ss


# In[753]:


product_pairs_products


# In[754]:


np.sum(product_pairs_products)


# In[ ]:





# In[755]:


#sets_of_adjacents[1][10][0:2]


# In[756]:


sets_of_adjacents[0][0]


# In[757]:


[0,55] == sets_of_adjacents[0][0][0:2]


# In[758]:


sets_of_adjacents[0][0][0:2]


# In[759]:


len(sets_of_adjacents[3])


# In[760]:


import sys
sys.path.append(os.pardir)
from src.HelperFunctions import convert_to_py

convert_to_py('3')

