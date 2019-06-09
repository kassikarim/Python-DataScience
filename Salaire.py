# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:24:49 2019
@author: kassi Abdelkrim
"""


#Import Python Libraries
import numpy as np
import pandas as pd

#Example of creating Pandas series :
S1 = pd.Series(np.random.randn(5))
print(S1)
print(S1.index)

# Creating Pandas series with index:
S1 = pd.Series(np.random.randn(5), index = ['a', 'b', 'c', 'd', 'e'])
print(S1.index)
print(S1)

# Series can be used as ndarray:
print("Median =" , S1.median())
print("Mean =", S1.mean())
print(S1[ S1 > 0 ])

S1.dtype
S1.head(2)

