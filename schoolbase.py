# Program that supports the school base
# Assign three types of users to classes and a teacher to a subject

import sys

phrase = sys.argv[1:]
print(sys.argv)

# lists and dictionaries:

educators = []
teachers = []
students = []
class_list = []
school_class = {}

users = "uczeń", "nauczyciel", "wychowawca", "koniec"


class Educator:

    def __init__(self, name):
        self.name = name
        self.school_class = self.class_choice()
        self.class_list = []


    def class_choice(self):
        while True:
            class_nr = input("\nWprowadź numer klasy: \nJeśli nie ma więcej danych do wprowadzenia, wciśnij *ENTER*\n")
            if class_nr == "":
                return class_list
            if class_nr not in school_class:
                school_class[class_nr] = class_nr
                class_list.append(class_nr)
                educators.append(name)


class Teacher:

    def __init__(self, name):
        self.name = name
        self.subject = self.subject_choice()
        self.school_class = self.class_choice()
        self.class_list = []

    def subject_choice(self):
        subject = input("\nWprowadź nazwę przedmiotu, którego uczy {}:\n".format(self.name))
        return subject

    def class_choice(self):
        while True:
            class_nr = input("\nWprowadź numer klasy: \nJeśli nie ma więcej danych do wprowadzenia, wciśnij *ENTER*\n")
            if class_nr == "":
                return class_list
            if class_nr not in school_class:
                school_class[class_nr] = class_nr
            class_list.append(class_nr)
            teachers.append(name)


class Student:

    def __init__(self, name):
        self.name = name
        self.class_nr = self.class_choice()
        students.append(name)

    def class_choice(self):
        self.class_nr = input("\nWprowadź nazwę klasy, do której uczęszcza {}\n".format(self.name))


while True:
    user = input("\nWybierz rodzaj użytkownika: uczeń, nauczyciel lub wychowawca.\nAby zakończyć wprowadź: koniec\n")
    if user == "koniec":
        print("\nWprowadzanie zakończone.\nPodsumowanie:\n")
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


if phrase[0] in class_list:
    print("Wychowawcą klasy {} jest .\nLista uczniów klasy:\n" .format(phrase[0]))
if phrase[0] in educators:
    print("Wychowawca {} jest opiekunem poniższych uczniów.\n" .format(phrase[0]))
if phrase[0] in teachers:
    print("Nauczyciel {} prowadzi lekcje w klasach, których wychowawcami są:\n" .format(phrase[0]))
if phrase[0] in students:
    print("Przedmioty ucznia {} to .\n" .format(phrase[0]))




