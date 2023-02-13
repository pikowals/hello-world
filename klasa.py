
#
# Auto1 = Car()
# Auto2 = Car
# Auto1.colour='czerwony'
# Auto1.type='kabriolet'
# Auto1.value='600000'
# Auto1.name='Ferrari'
# Auto2.colour='niebieski'
# Auto2.type='autobus'
# Auto2.value='100000'
# Auto2.name='Icarus'
#
# print(Auto2.name)

# kontakty = {}
# kontakty["Jan"] = 938477566
# kontakty["Jacek"] = 938377264
# kontakty["Janusz"] = 947662781
#
# for imie, numer in kontakty():
#     print("%s ma numer telefonu: %d" % imie, numer)
import copy
base = {1: "Jakub", 2: "Piotr", 4: "Paweł", 14: "John"}
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("Init klasy bazowej")
        print(f'Zmienna name ma wartosc {self.name}')
    def worker(self):
        if self.name in base.values():
            key_list = list(base.keys())
            value_list =list(base.values())
            pos = value_list.index(self.name)
            print(f"Osobnik o imieniu {self.name} jest pracownikiem i posiada ID: {key_list[pos]}")

        else:
            print(f"Osobnik o imieniu {self.name} nie jest w bazie pracowników")
    def introdcueWorker(self):
        print("Podaj nowy ID pracownika: ")
        ID = input()
        base[ID] = self.name # Wprowadzanie nowych wpisów do słownika



class Employee(Person):
    def __init__(self, id):
        self.id = id
        print(f"Pracownik ma ID {self.id}")
    def worker(self):
        if self.id in base:
            print(f"Pracownik o ID {self.id} jest obecnie zatrudniony")
        else:
            print(f"Pracownika o ID {self.id} niema w bazie")


p1 = Person("John", 37, "Male")
p1.worker()

# sprawdzić czy osoba jest w bazie pracownikow jesli tak to podać ID
# Sprawdzic czy pracownik jest w bazie jesli tak to wyswietlić Imie

p4 = Person("Janusz", 37, "Male")
p4.worker()
# p4.introdcueWorker()
import pprint
message = "Był jasny, zimowy dzień kwietniowy  zegary biły trzynasta"
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(pprint.pformat(count))

# p2 = Employee(14)
# p2.worker()

# print(p1.name)
# print(p1.age)
# print(p1.gender)

