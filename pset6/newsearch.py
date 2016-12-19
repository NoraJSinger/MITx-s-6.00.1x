# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:50:05 2016

@author: Nora Julianna kovacs
"""

def main():
    
    def newsearch(L, e):
        size = len(L)
        for i in range(size):
            if L[size-i-1] == e:
                return True
            if L[i] < e:
                    return False
        return False
    
    list = [2, 3, 7]
    num = 3
    
    if newsearch(list, num):
        print("true")
    else:
        print("false")
    
    
    
if __name__ == "__main__":
    main()