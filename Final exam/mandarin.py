# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 21:02:01 2016

@author: Nora Singer

Numbers in Mandarin follow 3 simple rules.

There are words for each of the digits from 0 to 10.
For numbers 11-19, the number is pronounced as "ten digit", so for example, 16 would be pronounced (using Mandarin) as "ten six".
For numbers between 20 and 99, the number is pronounced as “digit ten digit”, so for example, 37 would be pronounced (using Mandarin) as "three ten seven". If the digit is a zero, it is not included.
Here is a simple Python dictionary that captures the numbers between 0 and 10.

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
We want to write a procedure that converts an American number (between 0 and 99), written as a string, into the equivalent Mandarin.

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
"""

def main():
    
    def convert_to_mandarin(us_num):
        '''
        us_num, a string representing a US number 0 to 99
        returns the string mandarin representation of us_num
        '''
        trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
       
        if us_num in trans.keys():
            man_num = trans[us_num]
        elif len(us_num) == 2:
            if us_num[0] == '1':
                man_num = trans['10'] + ' ' + trans[us_num[1]]
            else:
                if us_num[1] == '0':
                    man_num = trans[us_num[0]] + ' ' + trans['10']
                else:
                    man_num = trans[us_num[0]] + ' ' + trans['10'] + ' ' + trans[us_num[1]]
                    
        return man_num
        
    number = '11'
    
    print (convert_to_mandarin(number))
        
if __name__ == "__main__":
    main()