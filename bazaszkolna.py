# Program that supports the school base
# Assign three types of users to classes and a teacher to a subject

import sys

phrase = sys.argv[1:]
print(sys.argv)

name_surname = ()
schoolmaster = ()
teachers = []
students = []
school_class = {}
subject = ()


class Klasy:
    def __init__(self, klasa):
        self.klasa = klasa
        self.wychowawca = input()
        self.nauczyciele = []
        self.uczniowe = []

def wybor_klasy():
    spis_klas = []
    while True:
        print("Wprowadź numer klasy")
        nr_klasy = input()
        if nr_klasy == "":
            return spis_klas
        if nr_klasy not in school_class.keys():
            school_class[nr_klasy] = Klasy(nr_klasy)
        spis_klas.append(nr_klasy)

class Wychowawca:
    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko

    def przypisanie_klasy(self):
        self.klasa = wybor_klasy()
        for k in self.klasa:
            k.wychowawca = self.imie_nazwisko

class Nauczyciel:
    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko

    def przypisanie_klasy(self):
        self.przedmiot = input()
        self.klasa = wybor_klasy()
        for k in self.klasa:
            k.nauczyciele.append(self.imie_nazwisko)

class Uczen:
    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko

    def przypisanie_klasy(self):
        self.przedmiot = input()
        self.klasa = wybor_klasy()








#
# while True:
#     rodzaj = input().strip()
#     if rodzaj == "koniec":
#         break
#     if rodzaj == "nauczyciel":
#         osoba = Nauczyciel()
#     if rodzaj == "wychowawca":
#         osoba = Wychowawca()
#     if rodzaj == "uczen":
#         osoba = Uczen()
#     if osoba.nazwa not in osoby:
#         osoby[osoba.nazwa] = []
#     osoby[osoba.nazwa].append(osoba)
#
# if sys.argv[1] in osoby:
#     for osoba in osoby[sys.argv[1]]:
#         osoba.wyswietl()
#
# if sys.argv[1] in wychowawcy_klas:
#     print("Wychowawca: {}".format(wychowawcy_klas[sys.a