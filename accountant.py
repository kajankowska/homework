# Prosty system księgowy
# Rejestrowanie zmian dla poszczególnych operacji

import sys

operacje = (sys.argv[1:])
print(sys.argv)

actions = ["saldo", "zakup", "sprzedaż", "stop"]

# zmienne:

kwota = 0
ilosc = 0
kom = 0
saldo = 0
cena = 0
magazyn = {}

operacje_saldo = []
operacje_zakup = []
operacje_sprzedaz = []

while True:
    print("\nWprowadź operację, którą chcesz rozpocząć. \nDo wyboru: saldo, zakup, sprzedaż."
          "\n* Jeśli chcesz zakończyć, wprowadź: stop *")
    action = input()
    if action not in actions:
        print("Niepoprawna operacja! Wprowadź ponownie")
        continue

    if action == "saldo":
        print("\nWprowadź kwotę:")
        kwota = int(input())
        print("\nWprowadź komentarz:")
        kom = input()
        saldo += kwota
        operacje_saldo = [action, kwota, kom]

    if action == "zakup":
        print("\nWprowadź nazwę produktu:")
        ID = input()
        print("\nWprowadź cenę:")
        cena = int(input())
        print("\nWprowadź ilość:")
        ilosc = int(input())
        if ID in magazyn.keys():
            magazyn[ID] += ilosc
        else:
            magazyn[ID] = ilosc
        saldo -= cena * ilosc
        if cena < 0 or ilosc < 0 or saldo < 0:
            print("Błąd! Ujemna wartość")
            break
        operacje_zakup = [action, ID, cena, ilosc]

    if action == "sprzedaż":
        print("\nWprowadź nazwę produktu:")
        ID = input()
        if ID not in magazyn.keys():
            print("Towar niedostępny w magazynie. Wprowadź ponownie.")
            continue
        else:
            magazyn[ID] -= ilosc
        print("\nWprowadź cenę:")
        cena = int(input())
        print("\nWprowadź ilość:")
        ilosc = int(input())
        if ilosc < magazyn[ID]:
            print("Niewystarczająca ilość towaru w magazynie.")
            break
        if cena < 0 or ilosc < 0:
            print("Błąd! Ujemna wartość")
            break
        saldo += cena * ilosc
        operacje_sprzedaz = [action, ID, ilosc, ilosc]

    if action == "stop":
        print("\nWprowadzanie zakończone. \nPodsumowanie:")
        break

if operacje[0] == "saldo":
    print("")
if operacje[0] == "sprzedaż":
    print("")
if operacje[0] == "zakup":
    print("")
if operacje[0] == "konto":
    print("\nWartość salda po wykonanych operacjach: ", saldo)
if operacje[0] == "magazyn":
    for k, v in magazyn.items():
        print("{}: {}".format(k, v))
if operacje[0] == "przegląd":
    print("")