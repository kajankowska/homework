# Program that supports the school base
# Assign three types of users to classes and a teacher to a subject

import sys

phrase = sys.argv[1:]
print(sys.argv)

# lists and dictionaries:

educators = {}
teachers = {}
students = {}
school_class = {}

class_list = []
class_data = []


users = "uczeń", "nauczyciel", "wychowawca", "koniec"


class Educator:

    def __init__(self, name):
        self.name = name
        self.class_list = []
        self.class_assign()
        educators[self.name] = self.class_list

    def class_assign(self):
        while True:
            class_nr = input("\nWprowadź numer klasy: \nJeśli nie ma więcej danych do wprowadzenia, wciśnij *ENTER*\n")
            if class_nr == "":
                return class_list
            if class_nr not in self.class_list:
                self.class_list.append(class_nr)
                class_data.append(class_nr)


class Teacher:

    def __init__(self, name):
        self.name = name
        self.subject = self.subject_choice()
        self.class_list = []
        self.class_assign()
        teachers[self.name] = self.class_list

    def subject_choice(self):
        subject = input("\nWprowadź nazwę przedmiotu, którego uczy {}:\n".format(self.name))
        return subject

    def class_assign(self):
        while True:
            class_nr = input("\nWprowadź numer klasy: \nJeśli nie ma więcej danych do wprowadzenia, wciśnij *ENTER*\n")
            if class_nr == "":
                return class_list
            if class_nr not in self.class_list:
                self.class_list.append(class_nr)
                class_data.append(class_nr)


class Student:

    def __init__(self, name):
        self.name = name
        self.class_assign()
        students[self.name] = self.class_nr

    def class_assign(self):
        self.class_nr = input("\nWprowadź nazwę klasy, do której uczęszcza {}\n".format(self.name))
        class_data.append(self.class_nr)


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


if phrase[0] in class_data:
    for k, v in educators.items():
        print("Wychowawcą klasy {} jest {}." .format(phrase[0], k) + "\nLista uczniów klasy:\n")
    for k, v in students.items():
        print("{}".format(k))
if phrase[0] in educators:
    print("Wychowawca {} jest opiekunem poniższych uczniów:\n" .format(phrase[0]))
if phrase[0] in teachers:
    print("Nauczyciel {} prowadzi lekcje w klasach, których wychowawcami są:\n" .format(phrase[0]))
if phrase[0] in students:
    print("Przedmioty ucznia {} to .\n" .format(phrase[0]))
