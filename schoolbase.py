# Program that supports the school base
# Assign three types of users to classes and a teacher to a subject

import sys

phrase = sys.argv[1:]
print(sys.argv)

# variables

name = ()
educator = ()
teachers = []
students = []
class_list = []
school_class = {}
class_choice = ()

user = ["uczeń", "nauczyciel", "wychowawca", "koniec"]


class SchoolClasses:

    def __init__(self, school_class):
        self.school_class = school_class
        self.educator = input()
        self.teachers = []
        self.students = []

    def class_choice(self):
        class_list = []
        while True:
            print("Wprowadź numer klasy")
            class_nr = input()
            if class_nr == "":
                return class_list
            if class_nr not in school_class.keys():
                school_class[class_nr] = SchoolClasses(class_nr)
            class_list.append(class_nr)


class Educator:

    def __init__(self, name):
        self.name = name

    def class_assign(self):
        self.class_nr = class_choice
        for k in self.class_nr:
            k.educator = self.name


class Teacher:

    def __init__(self, name):
        self.name = name

    def class_assign(self):
        self.subject = input()
        self.school_class = class_choice
        for k in self.class_nr:
            k.teachers.append(self.name)


class Student:

    def __init__(self, name):
        self.name = name

    def class_assign(self):
        class_nr = input()
        if class_nr not in school_class.keys():
            school_class[class_nr] = SchoolClasses(class_nr)
        self.class_nr = SchoolClasses(class_nr)
        self.class_nr.students.append(self.name)

while True:
    users = input("\nWybierz rodzaj użytkownika. \nDo wyboru: uczeń, nauczyciel, wychowawca."
                  "\n* Jeśli chcesz zakończyć, wprowadź: koniec *\n")
    if user == "koniec":
        print("\nWprowadzanie zakończone. Przejdź do podsumowania.")
        break
    elif user not in users:
        print("\nNiepoprawne dane. Wprowadź ponownie")
        continue
    else:
        name = input("Podaj imię i nazwisko użytkownika")
        if user == "uczeń":
            student = input("Wprowadź nazwę klasy, do której uczęszcza {}".format(name))
            continue
        if user == "nauczyciel":
            subject = input("Wprowadź nazwę przedmiotu, którego uczy {}".format(name))
        if user == "wychowawca":
            class_list


