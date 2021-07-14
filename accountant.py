# Simple accounting system
# Recording changes for individual operations

import sys

operation = (sys.argv[1:])
print(sys.argv)

actions = ["saldo", "zakup", "sprzedaż", "stop"]

# variables:

amount = 0
quantity = 0
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
        product_name = input()
        print("\nWprowadź cenę:")
        price = int(input())
        print("\nWprowadź ilość:")
        quantity = int(input())
        if balance < price * quantity:
            print("Niewystarczająca ilość środków na zakup")
            continue
        if product_name in storage.keys():
            storage[product_name] += quantity
        else:
            storage[product_name] = quantity
        balance -= price * quantity
        if price < 0 or quantity < 0:
            print("Błąd! Ujemna wartość")
            continue
        log = f'{action} -- {product_name} -- {price} -- {quantity}'
        sys_actions.append(log)

    if action == "sprzedaż":
        print("\nWprowadź nazwę produktu:")
        product_name = input()
        if product_name not in storage.keys():
            print("Towar niedostępny w magazynie. Wprowadź ponownie.")
            continue
        print("\nWprowadź cenę:")
        price = int(input())
        print("\nWprowadź ilość:")
        quantity = int(input())
        if storage[product_name] < quantity:
            print("Niewystarczająca ilość towaru w magazynie.")
            continue
        else:
            storage[product_name] -= quantity
        if price < 0 or quantity < 0:
            print("Błąd! Ujemna wartość")
            break
        balance += price * quantity
        log = f'{action} -- {product_name} -- {price} -- {quantity}'
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