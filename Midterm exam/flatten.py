# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 09:49:57 2016

@author: Nora Singer
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
  
"""



def main():
    
    a = [2, [3]]
    
    def flatten(aList):
        return flatten(aList[0]) + (flatten(aList[1:]) if len(aList) > 1 else []) if type(aList) is list else [aList]
        
        
            
    print(flatten(a))
    


if __name__ == "__main__":
    main()