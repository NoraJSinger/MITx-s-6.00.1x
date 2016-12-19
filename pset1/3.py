# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:28:52 2016

@author: Nora Julianna kovacs
"""


    
    
    


def main():
    s = input("Enter a string: ")
    
    currentss = longestss = s[0]
    for letter in s[1:]:
        if letter >= currentss[-1]:
            currentss += letter
            if len(currentss) > len(longestss):
                longestss = currentss
        else:
            currentss = letter
    
    
    
    
    
    
    print("Longest substring in alphabetical order is: " + longestss)

if __name__ == "__main__":
    main()