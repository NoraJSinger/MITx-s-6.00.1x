# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:01:01 2016

@author: Nora Julianna kovacs
"""

def main():
    balance = eval(input("Enter the initial balance: "))
    annualInterestRate = eval(input("Enter the annual interest rate as a decimal: "))
    monthlyPaymentRate = eval(input("Enter the minimum monthly payment rate as a decimal: "))

    monthlyInterestRate = annualInterestRate / 12
    
    for month in range(12):
        minMonthlyPayment = balance * monthlyPaymentRate
        monthlyUnpaidBalance = balance - minMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate)
        
    
    balance = round(balance,2)
    print("Remaining balance: " + str(balance))
    
     
        


if __name__ == "__main__":
    main()
   