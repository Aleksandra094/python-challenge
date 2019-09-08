# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:51:30 2019

@author: Ola
Python challenge by kodolamacz.pl
Task 5: Advanced object oriented programming
"""

from abc import ABC, abstractmethod
import math

class Figura(ABC):

    @abstractmethod
    def obwod(self): 
        pass
    
    @abstractmethod
    def pole(self): 
        pass

    @abstractmethod
    def nazwa_figury(self):
        pass

    def informacje(self):
        print(f'{self.nazwa_figury()} o obwodzie {round(self.obwod(),1)} cm i polu {round(self.pole(), 1)} cm2.')

class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien

    def obwod(self):
        return 2 * math.pi * self.promien

    def pole(self):
        return math.pi * self.promien ** 2

    def nazwa_figury(self):
        return "Kolo"

    def informacje(self):
        super().informacje()
        print(f'Promien kola ma dlugosc {self.promien} cm.\n')

class Trojkat(Figura):
    def __init__(self, dlugoscBoku1, dlugoscBoku2, dlugoscBoku3):
        self.dlugoscBoku1 = dlugoscBoku1
        self.dlugoscBoku2 = dlugoscBoku2
        self.dlugoscBoku3 = dlugoscBoku3

    def obwod(self):
        return self.dlugoscBoku1 + self.dlugoscBoku2 + self.dlugoscBoku3

    def pole(self):
        p = self.obwod()/2
        return math.sqrt(p * (p-self.dlugoscBoku1) * (p-self.dlugoscBoku2) * (p-self.dlugoscBoku3))

    def nazwa_figury(self):
        return "Trojkat"

    def informacje(self):
        super().informacje()
        print(f'Boki trojkata maja dlugosc {self.dlugoscBoku1} cm, {self.dlugoscBoku2} cm i {self.dlugoscBoku3} cm.\n')

class Prostokat(Figura):
    def __init__(self, dlugoscBoku1, dlugoscBoku2):
        self.dlugoscBoku1 = dlugoscBoku1
        self.dlugoscBoku2 = dlugoscBoku2

    def obwod(self):
        return 2 * (self.dlugoscBoku1 + self.dlugoscBoku2)

    def pole(self):
        return self.dlugoscBoku1 * self.dlugoscBoku2

    def nazwa_figury(self):
        return "Prostokat"

    def informacje(self):
        super().informacje()
        print(f'Boki prostokata maja dlugosc {self.dlugoscBoku1} cm i {self.dlugoscBoku2} cm.\n')

class Kwadrat(Prostokat):
    def __init__(self, dlugoscBoku):
        self.dlugoscBoku1 = dlugoscBoku
        # Kwadrat jest prostokatem o rownych bokach
        self.dlugoscBoku2 = dlugoscBoku

    def nazwa_figury(self):
        return "Kwadrat"

    def informacje(self):
        super(Prostokat, self).informacje()
        print(f'Bok kwadratu ma dlugosc {self.dlugoscBoku1} cm.\n')


def test():
    Kolo(10).informacje()
    Trojkat(5, 6, 9).informacje()
    Prostokat(2, 10).informacje()
    Kwadrat(4).informacje()

if __name__ == "__main__":
    test()
