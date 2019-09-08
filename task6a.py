# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 21:35:49 2019

@author: Ola
Python challenge by kodolamacz.pl
Task 6: Exceptions in mathematical expressions
"""

from abc import ABC, abstractmethod
import math

class Wezel(ABC):
    @abstractmethod
    def nazwa(self):
        pass

    @abstractmethod
    def oblicz_wartosc(self):
        pass

    def informacje(self):
        print(f"Wynikiem operacji {self.nazwa()} jest wartosc {self.oblicz_wartosc()} \n")

class Wartosc(Wezel):
    def __init__(self, czynnik):
        self.czynnik = czynnik

    def nazwa(self):
        return "wartosc"

    def oblicz_wartosc(self):
        return float(self.czynnik)

class Suma(Wezel):
    def __init__(self, czynnik1, czynnik2):
        self.czynnik1 = czynnik1.oblicz_wartosc()
        self.czynnik2 = czynnik2.oblicz_wartosc()

    def nazwa(self):
        return "sumowania"

    def oblicz_wartosc(self):
        return self.czynnik1 + self.czynnik2

    def informacje(self):
        print(f"Liczby do operacji matematycznej: {self.czynnik1}, {self.czynnik2}")
        super().informacje()
        
class Roznica(Wezel):
    def __init__(self, czynnik1, czynnik2):
        self.czynnik1 = czynnik1.oblicz_wartosc()
        self.czynnik2 = czynnik2.oblicz_wartosc()

    def nazwa(self):
        return "odejmowania"

    def oblicz_wartosc(self):
        return self.czynnik1 - self.czynnik2

    def informacje(self):
        print(f"Liczby do operacji matematycznej: {self.czynnik1}, {self.czynnik2}")
        super().informacje()

class Iloczyn(Wezel):
    def __init__(self, czynnik1, czynnik2):
        self.czynnik1 = czynnik1.oblicz_wartosc()
        self.czynnik2 = czynnik2.oblicz_wartosc()

    def nazwa(self):
        return "mnozenia"

    def oblicz_wartosc(self):
        return self.czynnik1*self.czynnik2

    def informacje(self):
        print(f"Liczby do operacji matematycznej: {self.czynnik1}, {self.czynnik2}")
        super().informacje()

class Iloraz(Wezel):
    def __init__(self, czynnik1, czynnik2):
        self.czynnik1 = czynnik1.oblicz_wartosc()
        if czynnik2.oblicz_wartosc == 0:
            raise ZeroDivisionError("Dzielnik jest zerem. Nie mozna zrealizowac operacji.")
        else:
            self.czynnik2 = czynnik2.oblicz_wartosc()

    def nazwa(self):
        return "dzielenia"

    def oblicz_wartosc(self):
        return self.czynnik1/self.czynnik2

    def informacje(self):
        print(f"Liczby do operacji matematycznej: {self.czynnik1}, {self.czynnik2}")
        super().informacje()

class Silnia(Wezel):
    def __init__(self, czynnik):
        if czynnik.oblicz_wartosc() < 0:
            raise ValueError("Operacja silni nie moze zostac wykonana na liczbach mniejszych od zera.")
        else:
            self.czynnik = czynnik.oblicz_wartosc()

    def nazwa(self):
        return "silni"

    def oblicz_wartosc(self):
        return math.factorial(self.czynnik)

    def informacje(self):
        print(f"Liczby do operacji matematycznej: {self.czynnik}")
        super().informacje()

class Ulamek:

    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        if mianownik == 0:
            raise ZeroDivisionError("Nie mozna utworzyc ulamka o mianowniku 0.")
        else:
            self.mianownik = mianownik

    def __repr__(self):
        return f'{self.licznik}/{self.mianownik}'

    def skroc(self):
        if self.licznik == 0:
            self.mianownik = 1
        else:
            #Poszukiwanie najwiekszego wspolnego mianownika metoda Euklidesa
            a = max(self.licznik, self.mianownik)
            b = min(self.licznik, self.mianownik)
            c = a - b
            lista = [a, b, c]
            while c!=0:
                lista.sort()
                c = lista[1]-lista[0]
                lista.append(c)
            nwd = lista[0]
    
            self.licznik //= nwd
            self.mianownik //= nwd
        
        return self

    @staticmethod
    def dodaj(ulamek1, ulamek2):
        return Ulamek(ulamek1.licznik * ulamek2.mianownik + ulamek2.licznik*ulamek1.mianownik, ulamek1.mianownik*ulamek2.mianownik)

    @staticmethod
    def odejmij(ulamek1, ulamek2):
        return Ulamek(ulamek1.licznik * ulamek2.mianownik - ulamek2.licznik*ulamek1.mianownik, ulamek1.mianownik*ulamek2.mianownik)

    @staticmethod
    def mnoz(ulamek1, ulamek2):
        return Ulamek(ulamek1.licznik*ulamek2.licznik, ulamek1.mianownik*ulamek2.mianownik)

    @staticmethod
    def dziel(ulamek1, ulamek2):
        if ulamek2.licznik == 0:
            raise ZeroDivisionError("Dzielnik jest rowny zero. Nie mozna zrealizowac operacji.")
        return Ulamek(ulamek1.licznik*ulamek2.mianownik, ulamek1.mianownik*ulamek2.licznik)

def calculator():
    decision = "t"
    while decision=="t":
        # Show the calculator's instruction
        print("Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, następnie kolejną liczbę:")
        
        # Get the inout data
        try:
            number1 = float(input())
            operator = input()
            number2 = float(input())
        except ValueError:
            print("Zamiast liczby podano inny znak")
            break

        # Interpretation of the operator
        if operator is "+":
            wynik = number1 + number2

        elif operator is "-":
            wynik = number1 - number2

        elif operator is "*":
            wynik = number1 * number2

        elif operator is "/":
            try:
                wynik = number1 / number2
            except ZeroDivisionError:
                print("Nie mozna wykonac dzielenia przez zero")
                break

        elif operator is "%":
            try:
                wynik = number1 % number2
            except ZeroDivisionError:
                print("Nie mozna wykonac operacji modulo przez zero")
                break

        # Print the result
        print("Twój wynik to: ", wynik)
        
        # End or continue the calculations?
        print("Chcesz wynikać kolejne działanie? Wpisz literę t lub n.")
        decision = input()
        if decision=="t":
            continue
        elif decision=="n":
            break

if __name__ == "__main__":
    liczba1 = Wartosc(-1)
    liczba2 = Wartosc(2)
    suma = Suma(liczba1, liczba2)
    suma.informacje()
    roznica = Roznica(liczba1, liczba2)
    roznica.informacje()
    iloczyn = Iloczyn(liczba1, liczba2)
    iloczyn.informacje()
    iloraz = Iloraz(liczba1, liczba2)
    iloraz.informacje()
    silnia = Silnia(liczba1)    
    silnia.informacje()
#    ulamek = Ulamek(0, 5)
#    ulamek.skroc()
#    print(ulamek)
#    zly_ulamek = Ulamek(2, 3)
#    print(zly_ulamek)
#    Ulamek.dziel(zly_ulamek, ulamek)
#    calculator()