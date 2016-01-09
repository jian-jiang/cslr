# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:47:03 2016

@author: jian-jiang
"""

def search(A, key):
    # Return the index s.t. A[index] = key
    for i in range(0,len(A)):
        if A[i] == key:
            return i

    return None