import sys
import os
import csv
import json
import pickle
import pathlib

src_filepath = sys.argv[1]  # filetype: csv, json or pickle
dst_filepath = sys.argv[2]
newdata = sys.argv[3:]
changes = []
fields = []

if os.path.exists(src_filepath):
    print(f"\nŚcieżka do pliku: {src_filepath}.\n")


class FileReading():

    def csv_type(input):
        with open((sys.argv[1]), "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                fields.append(row)

    def json_type(input):
        with open(sys.argv[1], "r") as file:
            input += json.loads(file.read())
            return True

    def pickle_type(input):
        with open(sys.argv[1], "rb") as file:
            input += pickle.loads(file.read())
            return True

    if src_filepath == "csv":
        csv_type(input)
    if src_filepath == "json":
        json_type(input)
    if src_filepath == "csv":
        pickle_type(input)


if not os.path.exists(src_filepath) or not os.path.isfile(src_filepath):
    print(f"\nNie można odnaleźć pliku!\n" + f"Zawartość wskazanej lokalizacji:\n{os.listdir()}")

for change in sys.argv[3:]:
    changes.append(change.split(","))

for change in changes:
    if int(change[0]) > len(newdata[0]):
        print("Błędna liczba wierszy!")
        exit()
    if int(change[1]) > len(newdata[0]):
        print("Błędna liczba kolumn!")
        exit()
    fields[int(change[0])][int(change[1])] = change[2]

for i in fields:
    print(i)

with open((sys.argv[2]), "w", newline="", encoding="utf-8") as csvoutfile:
    writer = csv.writer(csvoutfile)
    for row in fields:
        writer.writerow(row)
print(f"\nPlik został zapisany w lokalizacji: {dst_filepath}.")
