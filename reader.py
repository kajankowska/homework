import sys
import os
import csv


src_filepath = sys.argv[1]
dst_filepath = sys.argv[2]
changes = sys.argv[3:]
print(sys.argv)

fields = []
row_nr = Y
column_nr = X

with open("src_filepath", newline="") as f:
    reader = csv.reader(f)
    for line in reader:
        fields.append(line)

    if not os.path.exists("src.filepath"):
        for i in range(len(os.listdir())):
            print(f"Nie można odnaleźć pliku!\n" + f"Zawartość wskazanej lokalizacji:\n{os.listdir()[i]}")
    else:
        print(f"Plik znajduje się w lokalizacji: {src_filepath}.")
 
if len(changes) != len(fields[y]):
    print("Niepoprawna ilość argumentów! Wprowadź ponownie.")
else:
    print("Dane zaczytały się poprawnie.")
    
    
# to add:    
# validation of arguments
# making changes to the file

print(fields)

    
