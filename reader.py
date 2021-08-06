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
        
for line in fields:
     for element in line[:-1]:  # jedziemy po wszystkich elementach wiersza oprócz ostatniego
          file.write(str(element) + ",")  # po każdym przecinek
              file.write(str(line[-1] + "\n"))  # a po ostatnim enter
    

print(fields)

    
