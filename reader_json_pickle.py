import sys
import os
import csv
import json
import pickle
import pathlib


class File:
    def __init__(self):
        self.src_filepath = sys.argv[1]
        self.dst_filepath = sys.argv[2]
        self.newdata = sys.argv[3:]
        self.file_extenison = pathlib.Path(self.src_filepath)
        self.type_extension = self.file_extenison.suffix
        self.extension = self.type_extension
        self.changes = []
        self.fields = []

    def file_exist(self):
        if os.path.exists(self.src_filepath):
            print(f"\nFile path: {self.src_filepath}.\n")
        if not os.path.exists(self.src_filepath) or not os.path.isfile(self.src_filepath):
            print(f"\nFile not found!\n" + f"Location content:\n{os.listdir()}")

        # if self.extension == "csv":
        #     selection = CsvFile()
        # if self.extension == "json":
        #     selection = JsonFile()
        # if self.extension == "pickle":
        #     selection = PickleFile()

    def file_editing(self):
        for change in self.newdata:
            self.changes.append(change.split(","))
        for change in self.changes:
            if int(change[0]) > len(self.newdata[0]):
                print("Wrong number of rows!")
                return False
            if int(change[1]) > len(self.newdata[0]):
                print("Wrong number of columns!")
                return False
            self.fields[int(change[0])][int(change[1])] = change[2]

    def display(self):
        for i in self.fields:
            print(i)


class CsvFile(File):
    def __init__(self):
        super().__init__()

    def file_exist(self):
        super().file_exist()

    def readfile(self):
        with open(self.src_filepath, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.fields.append(row)

    def file_editing(self):
        super().file_editing()

    def display(self):
        super().display()

    def savefile(self):
        with open(self.dst_filepath, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            for row in self.fields:
                writer.writerow(row)
        print(f"\nThe file location: {self.dst_filepath}.")
        

class JsonFile(File):
    def __init__(self):
        super().__init__()

    def file_exist(self):
        super().file_exist()

    def readfile(self):
        with open(self.src_filepath, "r", newline="", encoding="utf-8") as json_file:
            self.fields = json.loads(json_file)

    def file_editing(self):
        super().file_editing()

    def display(self):
        super().display()

    def savefile(self):
        with open(self.dst_filepath, "w", newline="", encoding="utf-8") as outfile:
            outfile.write(json.dumps(self.fields))
        print(f"\nThe file location: {self.dst_filepath}.")


class PickleFile(File):
    def __init__(self):
        super().__init__()

    def file_exist(self):
        super().file_exist()

    def readfile(self):
        with open(self.src_filepath, "r", newline="", encoding="utf-8") as pickle_file:
            self.fields = pickle.loads(pickle_file)

    def file_editing(self):
        super().file_editing()

    def display(self):
        super().display()

    def savefile(self):
        with open(self.dst_filepath, "w", newline="", encoding="utf-8") as outfile:
            outfile.write(json.dumps(self.fields))
        print(f"\nThe file location: {self.dst_filepath}.")
