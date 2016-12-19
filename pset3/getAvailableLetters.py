# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:49:34 2016

@author: Nora Julianna kovacs
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