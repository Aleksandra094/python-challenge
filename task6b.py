# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:32:47 2019

@author: Ola
Task 6: Lines counting
"""

def zlicz_linie():
    sciezka_input = input("Podaj sciezke do pliku wejsciowego:")

    with open(sciezka_input) as f:
        suma_wierszy = 0
        for wiersz in f:
            suma_wierszy += 1
    f.close()
    print(f"W podanym pliku znajduje sie {suma_wierszy} linii.")
    sciezka_output = input("Podaj sciezke do pliku wynikowego:")
    nazwa_pliku_wejsciowego = sciezka_input.split("\\")[-1]
    with open(sciezka_output, 'w') as f:
        f.write(f"Plik {nazwa_pliku_wejsciowego} zawiera {suma_wierszy} wierszy.")
    f.close()
    return suma_wierszy

if __name__ == "__main__":
    zlicz_linie()