# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:50:05 2016

@author: Nora Singer
"""

"""Here is code for linear search that uses the fact that a set of elements is sorted in increasing order:"""

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
 
    
"""Consider the following code, which is an alternative version of search."""

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False



"""Which of the following statements is correct? You may assume that each function 
is tested with a list L whose elements are sorted in increasing order; for simplicity, 
assume L is a list of positive integers. 

Correct answer: search and newsearch return the same answers for lists L of length 0, 1, or 2. correct


"""

