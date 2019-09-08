# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 17:35:32 2018

@author: Ola
Python challenge by kodolamacz.pl
Task 2: The calculator
"""
def calculator():
    decision = "t"
    while decision=="t":
        # Show the calculator's instruction
        print("Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, następnie kolejną liczbę:")
        
        # Get the inout data
        number1 = int(input())
        operator = input()
        number2 = int(input())
    
        # Interpretation of the operator
        if operator is "+":
            wynik = number1 + number2
        elif operator is "-":
            wynik = number1 - number2
        elif operator is "*":
            wynik = number1 * number2
        elif operator is "/":
            wynik = number1 / number2
        elif operator is "%":
            wynik = number1 % number2

        # Print the result
        print("Twój wynik to: ", wynik)
        
        # End or continue the calculations?
        print("Chcesz wynikać kolejne działanie? Wpisz literę t lub n.")
        decision = input()
        if decision=="t":
            continue
        elif decision=="n":
            break

# Call the function
if __name__ == "__main__":
    calculator()