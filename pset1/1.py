# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""



def main():
    s = input("Your string: ")
    
    counter = 0
    for letter in s:
        if letter in "aeiou":
            counter += 1
    
    print("Number of vowels: " + str(counter))
    


if __name__ == "__main__":
    main()
