# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:57:14 2019

@author: Ola
Python challenge by kodolamacz.pl
Task 3: Algorythms and data structures
"""


def sprytne_potegowanie(podstawa, wykladnik):

    if wykladnik == 0:
        return 1
    if wykladnik % 2 == 1:
        return (sprytne_potegowanie(podstawa, int(wykladnik/2))**2) * podstawa
    else:
        return (sprytne_potegowanie(podstawa, int(wykladnik/2)))**2


def czyPalindrom(napis):
    return napis == napis[::-1]


def czyAnagram(napis1, napis2):

    lista1 = list(napis1)
    lista2 = list(napis2)

    lista1.sort()
    lista2.sort()

    return lista1 == lista2


def moda(lista):

    iloscWystepowan = []

    for i in range(0, len(lista)):
        iloscWystepowan.append(lista.count(lista[i]))

    return lista[iloscWystepowan.index(max(iloscWystepowan))]


def main():
    print("2^10 = " + str(sprytne_potegowanie(2, 10)))
    print("czyPalindrom(kajak) = " + str(czyPalindrom("kajak")))
    print("czyPalindrom(kobyla) = " + str(czyPalindrom("kobyla")))
    print("czyAnagram(kajak, jaakk) = " + str(czyAnagram("kajak", "jaakk")))
    print("czyAnagram(kobyla, boczek) = " + str(czyAnagram("kobyla", "boczek")))
    print("moda([1,6,4,7,2,8,6,7,6]) = " + str(moda([1,6,4,7,2,8,6,7,6])))


if __name__ == "__main__":
    main()