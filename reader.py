import sys
import os
import csv


src_filepath = sys.argv[1]
dst_filepath = sys.argv[2]
changes = sys.argv[3:]
print(sys.argv)

fields = []
row = Y
column = X

with open("src_filepath", newline="") as f:
    reader = csv.reader(f)
    for line in reader:
        fields.append(line)

    if not os.path.exists("src.filepath"):
        print("Nie można odnaleźć pliku!\n" + f"Zawartość wskazanej lokalizacji:\n{os.listdir(src_filepath)}.")
    else:
        print(f"Plik znajduje się w lokalizacji: {src_filepath}.")
 
