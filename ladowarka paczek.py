# Obsługa ładowarki paczek

# Dowolna liczba elementów wprowadzana przez użytkownika
# Pojemność każdej paczki - maksymalnie 20kg
# Dodawane elementy o wadze od 1 do 10kg

# zmienne iteracyjne
part = 0
parcel_weight = 0
parcel_nr = 1
part_sum = 0
max_weight = 20
empty_weight = 0
weight_difference = 0
max_weight_difference = 0


print("Wprowadź liczbę elementów")
num_parts = int(input())

for p in range(num_parts):
    print("Wprowadź wagę elementu")
    part = float(input())
    if part == 0:
        print("Wszystkie paczki zostały wprowadzone. Dziękuję!")
        break
    elif part > 10 or part < 1:
        print("Błędna waga komponentu!")
        break
    else:
         if parcel_weight + part > max_weight:
            parcel_weight = part
            part_sum += part
            weight_difference = max_weight - parcel_weight
            if weight_difference > max_weight_difference:
                max_weight_difference = weight_difference
            print("Paczka o nr {} została wysłana!".format(parcel_nr))
            parcel_nr += 1
         else:
            parcel_weight += part
            part_sum += part

print("Liczba wysłanych paczek: {}." .format(parcel_nr))
print("Liczba wysłanych kilogramów: {}." .format(part_sum))
print("Liczba \"pustych\" kilogramów: {}." .format((parcel_nr * 20) - part_sum))
print("Najwięcej \"pustych\" kilogramów: {} było w paczce nr: ." .format(weight_difference))



