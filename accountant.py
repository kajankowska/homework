# Simple accounting system
# Recording changes for individual operations

import sys

operation = (sys.argv[1:])
print(sys.argv)

actions = ["saldo", "zakup", "sprzedaż", "stop"]

# variables:

amount = 0
quantity = 0
comment = 0
balance = 0
price = 0
storage = {}

sys_actions = []

while True:
    action = input("\nWprowadź operację, którą chcesz rozpocząć. \nDo wyboru: saldo, zakup, sprzedaż."
                   "\n* Jeśli chcesz zakończyć, wprowadź: stop *\n")

    if action not in actions:
        print("Niepoprawna operacja! Wprowadź ponownie")
        continue

    if action == "saldo":
        print("\nWprowadź kwotę:")
        amount = int(input())
        print("\nWprowadź komentarz:")
        comment = input()
        balance += amount
        log = f'{action} -- {amount} -- {comment}'
        sys_actions.append(log)

    if action == "zakup":
        print("\nWprowadź nazwę produktu:")
        ID = input()
        print("\nWprowadź cenę:")
        price = int(input())
        print("\nWprowadź ilość:")
        quantity = int(input())
        if ID in storage.keys():
            storage[ID] += quantity
        else:
            storage[ID] = quantity
        balance -= price * quantity
        if price < 0 or quantity < 0 or balance < 0:
            print("Błąd! Ujemna wartość")
            continue
        log = f'{action} -- {ID} -- {price} -- {quantity}'
        sys_actions.append(log)

    if action == "sprzedaż":
        print("\nWprowadź nazwę produktu:")
        ID = input()
        if ID not in storage.keys():
            print("Towar niedostępny w magazynie. Wprowadź ponownie.")
            continue
        else:
            storage[ID] -= quantity
        print("\nWprowadź cenę:")
        price = int(input())
        print("\nWprowadź ilość:")
        quantity = int(input())
        if quantity < storage[ID]:
            print("Niewystarczająca ilość towaru w magazynie.")
            break
        if price < 0 or quantity < 0:
            print("Błąd! Ujemna wartość")
            break
        balance += price * quantity
        log = f'{action} -- {ID} -- {price} -- {quantity}'
        sys_actions.append(log)

    if action == "stop":
        print("\nWprowadzanie zakończone. \nPodsumowanie:")
        break

if operation[0] == "saldo" or "sprzedaż" or "zakup":
    print(sys_actions)
if operation[0] == "konto":
    print("\nStan salda po wykonanych operacjach: ", balance)
if operation[0] == "magazyn":
    for k, v in storage.items():
        print("{}: {}".format(k, v))
if operation[0] == "przegląd":
    print("Liczba wykonanych operacji:", (len(sys_actions)), "\nWprowadź zakres (od, do):")
    start = int(input())
    end = int(input())
    print(sys_actions[start:end])
