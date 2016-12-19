# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:07:47 2016

@author: Nora Singer

Hangman Game

Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, 
lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in 
lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'
When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to 
the user how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ). This is called 
usability - it's very important, when programming, to consider the usability of your program. If users find your program 
difficult to understand or operate, they won't use it!

For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and 
underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
"""

def main():
    
    def getGuessedWord(secretWord, lettersGuessed):
        
        printword = []
        
        for letter0 in secretWord:
            printword.extend('_')
            
        for i in range(len(lettersGuessed)):
            for j in range(len(secretWord)):
                if lettersGuessed[i] == secretWord[j]:
                    printword[j] = secretWord[j]
                    
        printstring = ''.join(printword)
        return printstring
                    
                    
                    
                    
            
          
    
    
    
    
    string = "lettuce"
    list = ['w', 'y', 'e', 't', 't', 'o', 'c', 'e']
    
    print(getGuessedWord(string, list))
    


if __name__ == "__main__":
    main()
