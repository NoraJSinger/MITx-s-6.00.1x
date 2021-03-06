# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:01:01 2016

@author: Nora Singer

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135 
So your program only prints out one thing: the remaining balance at the end of the year in the format:

Remaining balance: 4784.0
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
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
   
