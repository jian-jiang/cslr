# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:51:42 2016

@author: jian-jiang
"""

def binary_add(A, B):
    # A and B are two n-bit binary lists
    # e.g. [1,1,0] => 6
    C = [0]*(len(A)+1) # results would be a (n+1)-element array
    plusOne = 0
    for i in range(len(A)-1,-1,-1):
        temp = A[i] + B[i] + plusOne
        if temp >=2:
            plusOne = 1
            C[i + 1] = temp - 2
        else:
            plusOne = 0
            C[i + 1] = temp
    C[0] = plusOne
    return C