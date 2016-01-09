# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:41:26 2016

@author: jian-jiang
"""

def insertion_sort_nonic(A):
    # Sort list to a non-decreasing order
    for j in range(1,len(A)):
        key = A[j]
        #Insert A[j] into the sorted sequence A[0..j-1]
        i = j - 1
        
        while i >= 0 and A[i] < key:
            A[i+1] = A[i]
            i = i - 1
        
        A[i+1] = key
        
    return A
