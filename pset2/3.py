# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:17:39 2016

@author: Nora Julianna kovacs
"""

def main():
    balance = eval(input("Enter the initial balance: "))
    annualInterestRate = eval(input("Enter the annual interest rate as a decimal: "))
    
    monthlyInterestRate = annualInterestRate / 12.0
    lowerBound = balance / 12.0
    upperBound = balance * (1 + monthlyInterestRate) ** 12.0 / 12.0
    
    
    
    while True:
        lowestPayment = (lowerBound + upperBound) / 2.0
        originalBalance = balance
        for month in range(12):
            monthlyUnpaidBalance = originalBalance - lowestPayment
            interest = monthlyUnpaidBalance * monthlyInterestRate
            originalBalance = monthlyUnpaidBalance + interest
        
        if abs(originalBalance) <= 0.01:
            break

        if originalBalance > 0:
            lowerBound = lowestPayment
        else:
            upperBound = lowestPayment
    lowestPayment = round(lowestPayment,2)        
    print("Lowest Payment: " + str(lowestPayment))

            
            
if __name__ == "__main__":
    main()