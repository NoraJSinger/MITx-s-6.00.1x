# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:57:10 2016

@author: Nora Singer

Implement a function called closest_power that meets the specifications below.

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
"""

def main():
    def closest_power(base, num):
        exponent = 0
        while True:
            multi = base**exponent
            multi2 = base**(exponent-1)
            if multi == num:
                return exponent
            if (multi > num):
                if abs(multi-num) < abs(multi2-num):
                    return exponent
                else:
                    return (exponent-1)
            if (multi < num):
                exponent+=1
            

    print(closest_power(3,3))

if __name__ == "__main__":
    main()