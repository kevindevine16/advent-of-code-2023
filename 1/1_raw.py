#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import os
pd.set_option('display.max_rows', 10)


# In[2]:


data_path = os.path.join('Data','input.txt')
data = pd.read_csv(data_path)
data = data.T.reset_index().T.reset_index(drop = True)
data.rename(columns={0:'inputs'},inplace = True)


# In[3]:


txt = '42'

def FindCalibrationValuesPart1(txt:str)->int:
    FirstDigit = False
    SecondDigit = False

    for i in range(len(txt)):
        if txt[i].isdigit():
            FirstDigit = int(txt[i])
            break
        pass

    for i in range(len(txt)):
        if txt[-1-i].isdigit():
            SecondDigit = int(txt[-1-i])
            break
        pass
    row_int = FirstDigit*10+SecondDigit
    return row_int

FindCalibrationValuesPart1(txt = txt)


# In[4]:


data['outputs_part1'] = data['inputs'].apply(lambda txt: FindCalibrationValuesPart1(txt = txt))


# In[5]:


data['outputs_part1'].sum()


# In[6]:


def FindFirstDigitPart2(txt:str)->int:
    FirstDigit = False
    numsInOrder = ['one', 'two', 'three', 'four','five', 'six', 'seven', 'eight','nine']
    nums = ['one', 'two', 'six', 'four','five','nine', 'three', 'seven', 'eight']
    numKey = {numsInOrder[k]:int(k+1) for k in range(len(numsInOrder))}

    for i in range(len(txt)):

        if txt[i].isdigit():
            FirstDigit = int(txt[i])
            return FirstDigit

        else:
           for num in nums:
            if num == txt[i:i+len(num)]:
              FirstDigit = numKey[num] 
              return FirstDigit 

def FindSecondDigitPart2(txt:str)->int:
    SecondDigit = False
    numsInOrder = ['one', 'two', 'three', 'four','five', 'six', 'seven', 'eight','nine']
    nums = ['one', 'two', 'six', 'four','five','nine', 'three', 'seven', 'eight']
    numKey = {numsInOrder[k]:int(k+1) for k in range(len(numsInOrder))}

    for i in range(len(txt)):

        if txt[-1-i].isdigit():
            SecondDigit = int(txt[-1-i])
            return SecondDigit

        else:
           for num in nums:
            if num == txt[-len(num)-i:len(txt)-i]:
              SecondDigit = numKey[num] 
              return SecondDigit 


def FindCalibrationValuesPart2(txt:str)->int:
    FirstDigit = FindFirstDigitPart2(txt = txt) 
    SecondDigit = FindSecondDigitPart2(txt = txt)
    return FirstDigit*10+SecondDigit




# In[7]:


data['outputs_part2'] = data['inputs'].apply(lambda txt: FindCalibrationValuesPart2(txt = txt))


# In[8]:


data['outputs_part2'].sum()


# In[9]:


def convert_to_py(prefix:str):
    from IPython import get_ipython
    get_ipython().system(f'jupyter nbconvert --to script {prefix}.ipynb --output {prefix}_raw')

convert_to_py('1')

