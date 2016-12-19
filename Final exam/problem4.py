# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:14:50 2016

@author: Nora Singer

You are given the following definitions:

A run of monotonically increasing numbers means that a number at position k+1 in the sequence is greater than or equal to the number at position k in the sequence.
A run of monotonically decreasing numbers means that a number at position k+1 in the sequence is less than or equal to the number at position k in the sequence.
Implement a function that meets the specifications below.

def longest_run(L):
    
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
   
"""

def main():
    
    def longest_run(L):
       
        longestAsc = [L[0]]
        currentList = [L[0]]
        for el in L[1:]:
               if currentList[-1] <= el:
                   currentList.append(el)
                   if len(currentList) > len(longestAsc):
                       longestAsc = currentList
               else:
                   currentList = [el]
           
            
                
                
                
               
        longestDesc =[L[0]]
        currentL2 = [L[0]]        
        for el in L[1:]:
                if currentL2[-1] >= el:
                    currentL2.append(el)
                    if len(currentL2) > len(longestDesc):
                        longestDesc = currentL2
                        
                else:
                       currentL2 = [el]
            
            
                
        if len(longestAsc) > len(longestDesc):
            sum = 0            
            for i in longestAsc:
                sum = sum + i
        elif len(longestAsc) < len(longestDesc):
            sum = 0
            for i in longestDesc:
                sum = sum + i
        else:
            ascIndex = L.index(longestAsc[0])
            descIndex = L.index(longestDesc[0])
            if ascIndex < descIndex:
                sum = 0
                for i in longestAsc:
                    sum = sum + i
            if ascIndex > descIndex:
                sum = 0
                for i in longestDesc:
                    sum = sum + i
            if ascIndex == descIndex:
                sum = 0
                for i in longestDesc:
                    sum = sum + i
                
                    
        return sum
       
        
                
    L = [3, 3, 3, 3, 3]              
    
    print(longest_run(L))
    
if __name__ == "__main__":
    main()