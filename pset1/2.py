# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:10:57 2016

@author: Nora Julianna kovacs
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