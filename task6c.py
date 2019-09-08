# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:45:25 2019

@author: Ola
Task 6: Operations on files using os library
"""

import os
import datetime

def sprzatanie():

    sciezka = input("Podaj sciezke do folderu ktory chcesz uporzadkowac:")
    zawartosc_folderu = os.listdir(sciezka)
    miesiac_temu = datetime.datetime.now() - datetime.timedelta(days=30)

    for i, plik in enumerate(zawartosc_folderu):
        sciezka_do_pliku = os.path.join(sciezka, zawartosc_folderu[i])
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(sciezka_do_pliku)

        if size > 1024 and datetime.datetime.fromtimestamp(mtime) < miesiac_temu:
            os.remove(sciezka_do_pliku)

if __name__ == "__main__":
    sprzatanie()