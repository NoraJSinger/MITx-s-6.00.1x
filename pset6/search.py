# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:44:55 2016

@author: Nora Julianna kovacs
"""

def main():
    
    def search(L, e):
        for i in range(len(L)):
            if L[i] == e:
                return True
                if L[i] > e:
                    return False
        return False
    
    list = [2, 3, 7]
    num = 2
    
    if search(list, num):
        print("true")
    else:
        print("false")
    
    
    
if __name__ == "__main__":
    main()
    