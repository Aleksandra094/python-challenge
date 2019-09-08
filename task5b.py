# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:51:30 2019

@author: Ola
Python challenge by kodolamacz.pl
Task 5: Advanced object oriented programming
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
        self.czynnik = czynnik.oblicz_wartosc()
    def nazwa(self):
        return "silni"

    def oblicz_wartosc(self):
        return math.factorial(self.czynnik)

    def informacje(self):
        print(f"Liczby do operacji matematycznej: {self.czynnik}")
        super().informacje()


def test():
    liczba1 = Wartosc(6)
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

if __name__ == "__main__":
    test()