import sys

# zmienne

lista = (sys.argv[1:])
log = []
kupno = []
saldo = []
sprzedaz = []
akcja = lista[0]
akcja1 = lista[0:]
konto = 0
konto1 = 0
konto2 = 0
stop = []
magazyn = {}
nazwa = 0
ilosc = 0

# petla w przypadku wyboru salda sprzedazy lub kupna

while True:

    if konto < 0:
        print("konto nie moze byc ujemne")
        break

    akcja = input(str("Wybierz akcje którą chcesz wykonac \n"
                      "** saldo ** kupno ** sprzedaz ** \n"
                      " "))

    if akcja == "saldo":
        print("Podaj kwote: ")
        kwota = int(input())
        print("Podaj komentarz: ")
        komentarz = str(input())
        konto += kwota
        saldo = [akcja, kwota, komentarz]
        log.append(saldo)

    elif akcja == "kupno":
        print("Podaj nazwe produktu: ")
        nazwa = str(input())
        print("Podaj cene zakupu: ")
        cena = int(input())
        print("Podaj ilosc: ")
        ilosc = int(input())
        konto -= cena * ilosc
        if nazwa in magazyn.keys():
            magazyn[nazwa] += ilosc
        else:
            magazyn[nazwa] = ilosc
        kupno = [akcja, nazwa, cena, ilosc]
        log.append(kupno)

    elif akcja == "sprzedaz":
        print("Podaj nazwe produktu: ")
        nazwa = str(input())
        print("Podaj cene sprzedazy: ")
        cena = int(input())
        print("Podaj ilosc: ")
        ilosc = int(input())
        konto += cena * ilosc
        if nazwa in magazyn.keys():
            magazyn[nazwa] -= ilosc
        else:
            magazyn[nazwa] = ilosc
        sprzedaz = [akcja, nazwa, cena, ilosc]
        log.append(sprzedaz)

    elif akcja == "stop":
        stop = [akcja]
        log.append(stop)
        break

    else:
        print("błędne dane")
        break

for i in log:
    for j in i:
        print(j)

if lista[0] == "konto":
    print(konto)


if lista[0] == "magazyn":
    for i, k in magazyn.items():
        if k < 0:
            print("ilosc nie moze byc ujemna")
        else:
            print("{} : {} ".format(i, k))
    for id in lista[1:]:
        if id in magazyn.keys():
            print("{} : {} ".format(id, magazyn[id]))
        else:
            print("{} : {} ".format(id, 0))

if lista[0] == "przeglad":
    poczatek = int(lista[1])
    koniec = int(lista[2])
    for i in range(poczatek, koniec+1):
        print(log[i])