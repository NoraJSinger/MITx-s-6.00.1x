# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:21:30 2016

@author: Nora Julianna kovacs
"""

def main():
    balance = eval(input("Enter the initial balance: "))
    
    annualInterestRate = eval(input("Enter the annual interest rate as a decimal: "))

    originalBalance = balance
    monthlyInterestRate = annualInterestRate / 12 
    interestCount = 0
    
    monthlyPayment = balance / 12
    
    
    
    for month in range(12):
        monthlyUnpaidBalance = balance - monthlyPayment
        interest = monthlyUnpaidBalance * monthlyInterestRate
        interestCount = interestCount + interest
        balance = monthlyUnpaidBalance + interest
    
    medianInterest = interestCount / 12
    
    monthlyPayment = monthlyPayment + medianInterest
    monthlyPayment = monthlyPayment / 10
    monthlyPayment = int(monthlyPayment) * 10
    
    for month in range(12):
        UnpaidBalance = originalBalance - monthlyPayment
        originalBalance = UnpaidBalance + (UnpaidBalance * monthlyInterestRate)
        
    if originalBalance > 0:
        monthlyPayment = monthlyPayment + 10
    
    print("Lowest Payment: " + str(monthlyPayment))
    
        
    
  
    
if __name__ == "__main__":
    main()
        