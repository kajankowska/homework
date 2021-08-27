import sys
import os
import csv
import json
import pickle
import pathlib

src_filepath = sys.argv[1]
dst_filepath = sys.argv[2]
newdata = sys.argv[3:]
changes = []
fields = []


class File:
    def __init__(self):
        self.input_file = src_filepath
        self.output_file = dst_filepath
        self.newdata = sys.argv[3:]
        self.changes = []
        self.fields = []
        for change in self.newdata:
            self.changes.append(change.split(","))

    def file_editing(self):
        for change in self.changes:
            if int(change[0]) > len(self.newdata[0]):
                print("Wrong number of rows!")
                return False
            if int(change[1]) > len(self.newdata[0]):
                print("Wrong number of columns!")
                return False
            self.fields[int(change[0])][int(change[1])] = change[2]


class CsvFile:
    def __init__(self):
        super().__init__()

    def editing(self):
        with open(self.src_file, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.fields.append(row)


class Json:
    def __init__(self):
        super().__init__()


class Pickle:
    def __init__(self):
        super().__init__()
