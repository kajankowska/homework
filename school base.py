# Program that supports the school base. Assign three types of users to classes and a teacher to a subject

import sys

phrase = sys.argv[1:]
print(sys.argv)

teachers = {}
data = {}
students_list = []
class_list = []

users = "uczeń", "nauczyciel", "wychowawca", "koniec"


class SchoolClass:
    def __init__(self):
        self.educator = False
        self.students_list = []
        self.teachers = {}

    def student_assign(self, new_student):
        self.students_list.append(new_student)


class Educator:

    def __init__(self, name):
        self.name = name
        self.class_nr = ""
        self.class_list = []
        self.class_assign()
        self.educator_assign()

    def educator_assign(self):
        data[self.name] = self

    def class_assign(self):
        while True:
            class_nr = input("\nWprowadź numer klasy: \nJeśli nie ma więcej danych do wprowadzenia, wciśnij *ENTER*\n")
            if class_nr == "":
                return class_list
            if class_nr not in data:
                data[class_nr] = SchoolClass()
            data[class_nr].educator = self.name
            self.class_list.append(class_nr)


class Teacher:

    def __init__(self, name):
        self.name = name
        self.subject = self.subject_choice()
        self.class_nr = ""
        self.class_list = []
        self.class_assign()
        self.teacher_assign()

    def subject_choice(self):
        subject = input("\nWprowadź nazwę przedmiotu, którego uczy {}:\n".format(self.name))
        return subject

    def teacher_assign(self):
        data[self.name] = self

    def class_assign(self):
        while True:
            class_nr = input("\nWprowadź numer klasy: \nJeśli nie ma więcej danych do wprowadzenia, wciśnij *ENTER*\n")
            if class_nr == "":
                return class_list
            if class_nr not in data:
                data[class_nr] = SchoolClass()
            data[class_nr].teachers[self.subject] = self.name
            self.class_list.append(class_nr)


class Student:

    def __init__(self, name):
        self.name = name
        self.class_nr = ""
        self.class_list = []
        self.class_assign()
        self.student_assign()

    def class_assign(self):
        class_nr = input("\nWprowadź nazwę klasy, do której uczęszcza {}\n".format(self.name))
        if class_nr not in data:
            data[class_nr] = SchoolClass()
        data[class_nr].student = self.name
        self.class_list.append(class_nr)

    def student_assign(self):
        data[self.name] = self


while True:
    user = input("\nWybierz rodzaj użytkownika: uczeń, nauczyciel lub wychowawca.\nAby zakończyć wprowadź: koniec\n")
    if user == "koniec":
        print("\nWPROWADZANIE ZAKOŃCZONE.\nPODSUMOWANIE:\n")
        break
    if user not in users:
        print("\nNiepoprawne dane. Wprowadź ponownie")
        continue
    else:
        name = input("\nPodaj imię i nazwisko użytkownika:\n")
        if user == "uczeń":
            student = Student(name)
            continue
        if user == "nauczyciel":
            teacher = Teacher(name)
            continue
        if user == "wychowawca":
            educator = Educator(name)
            continue

# phrase specified class_nr:
if phrase[0] in data:
    print(f"Informacje o klasie {phrase[0]}:\n")
    if data[phrase[0]].educator:
        print(f"Wychowawcą klasy {phrase[0]} jest {data[phrase[0]].educator}.")
    if data[phrase[0]].students_list:
        print(f"Lista uczniów klasy: {data[phrase[0]].students_list}")

# phrase educator name:
if phrase[0] in data:
    print(f"Wychowawca {phrase[0]} jest opiekunem poniższych uczniów:")
    if data[phrase[0]].class_list:
        for class_nr in data[phrase[0]].class_list:
            print(data[class_nr].students_list)

# phrase teacher name:
if phrase[0] in data:
    print(f"Lista wychowawców klas, z którymi {phrase[0]} prowadzi zajęcia:")
    if data[phrase[0]].class_list:
        for class_nr in data[phrase[0]].class_list:
            print(data[class_nr].educator)

# phrase student name:
if phrase[0] in data:
    print(f"Lista zajęć (wraz z nauczycielami prowadzącymi), na które uczęszcza {phrase[0]}:")
    if data[phrase[0]].class_list:
        for class_nr in data[phrase[0]].class_list:
            print(data[class_nr].teachers)
