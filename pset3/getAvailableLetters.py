# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:49:34 2016

@author: Nora Singer

Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. 
This function returns a string that is comprised of lowercase English letters - all lowercase English letters that
are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:
"""

def main():
    def getAvailableLetters(lettersGuessed):
        
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        available = ''
    
        for letter in alphabet:
            if letter not in lettersGuessed:
                available += letter
            
        return available
                
                    
                    
       


    list = ['a', 'y', 'e', 'b', 'b', 'o', 'c', 'e']        
   
    print(getAvailableLetters(list))
    


if __name__ == "__main__":
    main()
