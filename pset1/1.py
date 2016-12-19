# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


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
