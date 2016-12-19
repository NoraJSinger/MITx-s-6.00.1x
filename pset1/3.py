# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:28:52 2016

@author: Nora Singer

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
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
