# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:36:36 2019

@author: Ola
Python challenge by kodolamacz.pl
Task 4: Object-oriented programming
"""

class FunkcjaKwadratowa:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Rozwiaz(self):
        # Przypadek gdy podana funkcja jest liniowa(a=0)
        if self.a == 0:
            # Podana funkcja jest liniowa o stalej wartosci(a=0 i b=0)
            if self.b == 0:
                if self.c == 0:
                    print(f"Podana funkcja jest liniowa o stalej wartosci 0.")
                    rozwiazanie = "Istnieje nieskonczenie wiele miejsc zerowych"
                else:
                    # Szczegolny przypadek funkcji liniowej stalej przyjmujacej w calej dziedzinie wartosc 0
                    print(f"Podana funkcja jest liniowa o stalej wartosci {self.c}.")
                    rozwiazanie = "Brak miejsc zerowych"
            # Z uwagi na a=0 i pozostale wspolcznniki rozne od zera, jest to funkcja liniowa postaci bx+c=0
            else:
                x=-self.c/self.b
                print(f"Podana funkcja jest funkcja liniowa o rozwiazaniu {x}")
                rozwiazanie = x

        # Wspolczynnik a rozny od zera gwarantuje ze podana funkcja zawsze bedzie kwadratowa
        else:
            delta = self.b ** 2 - 4 * self.a * self.c
            
            if delta < 0:
                print("Miejsca zerowe nie istnieja.")
                rozwiazanie = "Brak miejsc zerowych"
            elif delta == 0:
                x0 = (-self.b + (delta ** (1 / 2))) / (2 * self.a)
                print(f"Istnieje jedno miejsce zerowe x0 rowne {x0}.")
                rozwiazanie = x0
            else:
                x1 = (-self.b + (delta ** (1 / 2))) / (2 * self.a)
                x2 = (-self.b - (delta ** (1 / 2))) / (2 * self.a)
                print(f"Istnieja pierwiastki podanej funkcji: w x1 rownym {x1} oraz x2 rownym {x2}.")
                rozwiazanie = (x1, x2)
        return rozwiazanie
class Zespolona:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __repr__(self):
        if self.im < 0:
            return f'{self.re}{self.im}i'
        else:
            return f'{self.re}+{self.im}i'

    def modul(self):
        return (self.re**2+self.im**2)**(1/2)

    @staticmethod
    def dodaj(liczba1, liczba2):
        return Zespolona(liczba1.re+liczba2.re, liczba1.im+liczba2.im)

    @staticmethod
    def mnoz(liczba1, liczba2):
        return Zespolona(liczba1.re*liczba2.re-liczba1.im*liczba2.im, liczba1.re*liczba2.im+liczba2.re*liczba1.im)


class Ulamek:

    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def __repr__(self):
        return f'{self.licznik}/{self.mianownik}'

    def skroc(self):
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
        return Ulamek(ulamek1.licznik*ulamek2.mianownik, ulamek1.mianownik*ulamek2.licznik)

def test():
    ulamek1 = Ulamek(1, 2)
    ulamek2 = Ulamek(3, 4)
    dodawanie = Ulamek.dodaj(ulamek1, ulamek2)
    print(dodawanie)
    odejmowanie = Ulamek.odejmij(ulamek2, ulamek1)
    print(odejmowanie)
    mnozenie = Ulamek.mnoz(ulamek1, ulamek2)
    print(mnozenie)
    dzielenie = Ulamek.dziel(ulamek1, ulamek2)
    print(dzielenie)
if __name__ == "__main__":
    test()