# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:36:31 2016

@author: Nora Singer
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Implement a function that meets the specifications below.

def applyF_filterG(L, f, g):

    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty

"""

        
def main():
    def f(i):
       return i+2
    def g(i):
       return i>5

    def applyF_filterG(L,f,g):
        newL = []
        for element in L:
            if g(f(element)) is True:
                newL.append(element)
        L[:] = newL	
        return (max(L) if len(L) > 0 else None)
        
    
    
    L=[0,1,2]
    print(applyF_filterG(L,f,g))
    print(L)
   
    
if __name__ == "__main__":
    main()
