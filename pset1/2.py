# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:10:57 2016

@author: Nora Singer

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



def bobcounter(string):
    bob = "bob"
    
    counter = 0
    for index in range(len(string) - len(bob) + 1):
        if string[index:index + len(bob)] == bob:
            counter += 1
    return counter


def main():
    
    print("Number of times bob occurs is: " + str(bobcounter(s)))


if __name__ == "__main__":
    main()
