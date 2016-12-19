# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:31:38 2016

@author: Nora Singer

Implement a function that meets the specifications below.

def deep_reverse(L):
    assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    
   
"""

def main():
    def deep_reverse(L):
       for element in L:
           element.reverse()
       L.reverse()
       print(L)
       
    L = [[1,2], [3,4], [5,6,7]]   
    deep_reverse(L) 


if __name__ == "__main__":
    main()