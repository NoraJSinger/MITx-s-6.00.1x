# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:07:47 2016

@author: Nora Julianna kovacs
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