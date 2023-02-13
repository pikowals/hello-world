# class Person:
#     def __init__(self, name, age, gender):              # Kontruktor klasy, wywoływany przy każdym tworzeniu obiektu
#         self.name = name
#         self.age = age
#         self.gender = gender
#         print("Init klasy bazowej")
#         print(f'Zmienna name ma wartosc {self.name}')   # print (f) pozwala na przekazanie wartosci parametru z argumentu self.name
#     def introduce(self):
#         print(f"Mam na imie{self.name}")
# class Employee(Person):
#     def __init__(self):
#         Person.__init__(self, name, age, gender)
#         print("Init klasy pochodnej też w grze")
#
#
# p1 = Person("John", 37, "Male")
# """Inicjalizacja obiektu wartosciami - wywołanie inita"""
#
# print(p1.name)
# print(p1.age)
# print(p1.gender)
# e1 = Employee()
# print(e1.name)
# print(e1.age)
# e1.introduce()
#
# def deco(func):
#     def inside():
#         print(f"Function that has been started:{func.__name__}")
#     return inside
#
#
# @deco
# def first():
#     print("First function")
# @deco
# def second():
#     print("Second function")
#
# first()
# second()
# second()


# import time
#
# def dec(f):                                                                                                             # Declaration of decorator
#     def inside(*args,**kwargs):                                                                                         # Inside function of the decorator with all the arguments - function f is the original one
#         start = time.perf_counter()                                                                                     # Starting time
#         f(*args,**kwargs)                                                                                               # Initialization of the original function f
#         end = time.perf_counter()                                                                                       # ending time
#         print(f"How long function was running:,{f.__name__}, {start - end} ")                                           # Printing the function name that is being decorated and the time in which function was run
#     return inside
# @dec                                                                                                                    # Calling decorators
# def third(a,b):                                                                                                         # Function with 2 arguments
#     value = a*b
#     return value
# @dec
# def fourth(a,b,c):                                                                                                      # Function with 3 arguments
#     sum([a*b for i in range(c)])
#
# @dec
# def fifth(a):                                                                                                           # Function with 1 arguments
#     sum([a*a for i in range(a)])
#
#
# third(450,789)
# fourth(2,600,10000)
# fifth(40)

# import abc
# class Animal:
#     def __init__(self, gatunek, wielkość):                     #self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
#         self.gatunek = gatunek
#         self.wielkość = wielkość
#         print(self.gatunek)                    #The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on.
#     def increase_age(self):
#         print('pokaż mi swoją wielkość! ',self.wielkość )
# class Mammal(Animal):                                         #dziedziczenie z klasy bazowej Animal
#     def __init__(self, wielkość):                     #self w kazdej funkcji do reprezentacji instancji klasy i metod do ktorych mozemy się dostać
#         super().__init__("Ssak", wielkość)              #Dodatkowo, aby zainicjalizować zmienne z klasy bazowej w klasie podrzędnej musimy wywołać konstruktor klasy bazowej Animal.__init__(self) w konstruktorze klasy pochodnej.
#         print('Mammal!')
#     def introduce_yourself(self):
#         print('Jestem ', self.gatunek)
#
# class Cat(Animal):                          #Klasa Cat dziedziczy po klasie Mammal
#     def __init__(self, wielkość):
#         super().__init__("koteczek", wielkość)
#         print('Cat!')
#     def purr(self):
#         print('purr! ', self.gatunek)
# class Ptak(abc.ABC):
#     """Klasa abstrakcyjna"""
#     @abc.abstractmethod
#     def __init__(self, wielkość):
#         self.wielkość = wielkość
#
#
# cat_1 = Cat("Duzy")
# cat_1.increase_age()
# print(cat_1.gatunek, cat_1.wielkość)
# cat_1.purr()
# cat_1.increase_age()
#
# mammal_1 = Mammal("Ogromny")
# mammal_1.introduce_yourself()
# print(mammal_1.gatunek)
# #
# zwierz = Animal("zwierzak", "Normalny")
# zwierz.increase_age()



# class ptak:
#
#     def __init__(self, gatunek, szybkość):                                                                              #Konstruktor klasy nadrzędnej - ptak
#         self.gatunek = gatunek                                                                                          #Inicjalizacja zmiennych
#         self.szybkość = szybkość
#
#     def lec(self):
#         print("Tu", self.gatunek, ". Startuje, i zaraz osiągne prędkość", self.szybkość)                                #Przekazanie wartosci ze stworzonego obiektu do wyswietlenia
#
#     def wydajOdgłos(self):
#         print("glos")
#         pass
#
#
# class orzeł(ptak):                                                                                                      #Dziedziczenie z klasy nadrzędnej ptak do klasy podrzędnej orzeł
#
#     def __init__(self, szybkość):                                                                                       #Konstruktor klasy podrzednej orzeł (zawiera jeden argument) - przy tworzeniu obiektu typu orzeł, przekazujemy do konstruktora jeden argument/zmienną
#         super().__init__("orzeł", szybkość)                                                                             #Wywołane konstruktory klas potomnych, inicjują konstruktor klasy od której dziedziczą, za pomocą funkcji super ()
#                                                                                                                         #W tym przypadku obiekt orzełek przyjmuje jeden argument (w konstruktorze - szybkośc)
#                                                                                                                         #Natomiast wartość "orzełek" jest zainicjowana jako gatunek w klasie nadrzednej - ptak
#     def poluj(self):
#         print("Tu", self.gatunek, ". Rozpoczołem polowanie")                                                            #Metoda poluj dziedziczy zmienna gatunek z klasy ptak - dlatego jest widoczna w klasie orzeł
#
#
# class pingwin(ptak):
#
#     def __init__(self, szybkość):
#         super().__init__("pingwinek", szybkość)
#
#     def ślizgaj(self):
#         print("Tu", self.gatunek, ". Rozpoczołem ślizg")
#
#     def lec(self):
#         print("Tu", self.gatunek, ". Przykro mi, ale nie latam")
#
# p1 = pingwin("szybki")
# print(p1.szybkość)
# p1.ślizgaj()
# p2 = orzeł("błyskawiczny")
# print(p2.gatunek, p2.szybkość)
# p1.lec()
# p2.lec()
# p3=pingwin("wolny")
# print(p3.gatunek, p3.szybkość)
# p2.poluj()

#
#
# Accessories = {'lina': 1,'pochodnia':6,'złote monety':42,'sztylet':1,'strzała':12}
# dragonLoot =['złote monety','sztylet','złote monety','złote monety','ruby',]
#
#
#
# def displayInventory(inventory):
#     print('Inwentarz:')
#     item_total = 0
#     for k,v in inventory.items():
#         print(str(v) + " " + k)
#         item_total = item_total + v #Liczenie wszystkich itemow w słowniku
#     print("Całkowita liczba przedmiotów " + str(item_total))
# def addToInventory(inventory,addedItems):
#     for i in addedItems:            # Przechodzenie przez wszystkie indeksy listy
#         for k in inventory:         # Przechodzenie przez wszystkie klucze słownika
#             if i == k:              # Przyrownujemy czy wartosc pod indeksem listy jest równa wartosci klucza
#                 inventory[k] = inventory[k] + 1     # Jeśli tak - zwiększ wartośc danego klucza w słowniku o 1
#         inventory.setdefault(i, 1)  # W pozostałych przypadkach dodaj nowy klucz (nie istniejacy jeszcze) do slownika
#         # if i not in inventory:    # Druga metoda - tożsama z linia powyżej
#         #     inventory[i] = 1
#
#     return inventory
#
# displayInventory(Accessories)
# Accessories = addToInventory(Accessories,dragonLoot)
# displayInventory(Accessories)

#
#
# ciag = 'Witaj chłopie'
# ciag1 = 'Witaj chłopie z Somalii     '
#
#
#
# picnic = {'Jabłka': 4, 'Piwo': 6, 'Kiełbaski': 7, 'Szaszłyki': 10, 'Sałatka':1, 'Pieczywo': 2, 'Lody': 3}
# def picnicThings(picnicDic,leftWidth,rightwidth):
#     total_item=0
#     print('Rzeczy przyniesione na piknik:'.center(leftWidth+rightwidth,'-'))
#     for k,v in picnicDic.items():
#         print(k.ljust(leftWidth,'.') + str(v).rjust(rightwidth,' '))
#         total_item = total_item + v
#     print('Liczba wszystkich rzeczy: '.rjust(leftWidth,'|') + str(total_item))
# picnicThings(picnic,20,3)
# print(ciag.strip('i'))
# picnicThings(picnic,50,5)

import pyperclip
# # pyperclip.copy('Witaj Świecie') teraz kopiując słowo pyperclip przec ctrl+c i uruchamiajac kod otrzymały takie wpis
# print(pyperclip.paste())


# PASSWORDS = {'email': 'askja293821nnsdksf239r', 'blog': 'Ahw3298e32cjdsckjds','luggage': '11213332'}
#
# import sys, pyperclip
# if len(sys.argv) <2:
#     print('Uzycie: python pw.py [konto] - skopiownane hasła wskazanego konta')
#     sys.exit()
# acccount = sys.argv[1]
# if acccount in PASSWORDS:
#     pyperclip.copy(PASSWORDS[acccount])
#     print('Hasło do konta '+acccount+' zostało skopiowane do schowka.')
# else:
#     print('Nie istnieje konto o nazwie ' + acccount + '.')
# print(sys.argv[2])

# print(pyperclip.paste())

#! python3
# import pyperclip
# text = pyperclip.paste()
# lines = text.split('\n')
# for i in range(len(lines)):
#     lines[i] = '* ' + lines[i]
# text = '\n'.join(lines)
#
#
# pyperclip.copy(text)
# print(text)

table = [['jabłka','pomarancze','wiśnie','banany'],
         ['Alicja','Bob','Karol','Dawid'],
         ['psy','koty','łosie','gęsi']]

def printTable(charList):
    colWidth =[0]*len(charList)
    iterator = 0
    for i in charList:
        for j in i:
            colWidth[iterator] = len(max(i, key=len))
            # if colWidth[iterator]< len(j):    # Alternatywnie mozna to zrobić przez if'a
            #     colWidth[iterator] = len(j)     podstawianie najdłuzszych wartosci ciagów w liscie do indeksow listy colwidth
        iterator+=1
    x = 0
    for i in colWidth:                          # Sprawdzanie najdłuzszej kolumny w liscie colWidth
        if x < i:
            x = i

    # print(len(charList))
    # y = 0
    # z = 0
    for i in range(len(charList[0])):           # Sprawdzenie długości pierwszej zagnieżdżonej listy - pierwsze zapętlenie wykona się 4 razy
        for j in range(len(charList)):          # Sprawdzenie długości całej listy (ile list jest w liście charList) - 3 razy sie wykona pętla wewnętrzna
                print(charList[j][i].rjust(x), end=' ') # Wyswietlamy odpowednio pierwsze elementy każdej listy wewnetrzenj i tak dalej
        print('')


    # print(len(charList[0]))
    # print(len(charList))
    print(x)

printTable(table)
