# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:07:55 2016

@author: Nora Singer

Hangman Game

First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, 
lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are 
in lettersGuessed) and False otherwise.

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(isWordGuessed(secretWord, lettersGuessed))
False
For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
"""

def main():
    
    def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    counter = 0
        
    for letter in secretWord:
        if letter in lettersGuessed:
            counter += 1
            
    if counter == len(secretWord):
            return True
    else:
            return False
            
    
    
    
    
    string = "lettuce"
    list = ['w', 'l', 'e', 't', 't', 'u', 'c', 'e']
    
    print(isWordGuessed(string, list))
    


if __name__ == "__main__":
    main()
