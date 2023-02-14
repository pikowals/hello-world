# def greet(name):
#     print(f'Hello', name)
#     return f"Hello, {name}!"
# def simon(func):
#     return func("Simon")
# simon(greet)


# def respect(maybe):
#     def congrats():
#         return "Congrats, bro!"
#     def insult():
#         return "You're silly!"
#     if maybe == "yes":
#         return congrats
#     else:
#         return insult
#
#
# print(respect("yes")())
# print(respect("Brother")())

# def startstop(func):
#     def wrapper():
#         print("Starting...")
#         func()
#         print("Finished!")
#     return wrapper
#
# def roll():
#     print("Rolling on the floor laughing XD")
# # roll = startstop(roll)()
# odpal = startstop(roll)
# odpal()

import time
# def measuretime(func):                                              # 4.Definicja funkcji dekorującej przyjmującej jako argument funkcję
#     def wrapper1():                                                 # 5.Funkcja wewnętrzna funkcji dekorującej - rozszerza naszą funkcję podstawową o zliczenie czasu wykonania zadania 2.
#         starttime = time.perf_counter()                             # 6.Do zmiennej starttime przypisuje wartość obecnego czasu
#         func()                                                      # 7.Wywołujemy funkcję przekazaną jako argument do dekoratora - w naszym przypadku jest to funkcja wastetime
#         endtime = time.perf_counter()                               # 8.Do zmiennej endtime przypisuje wartość obecnego czasu
#         print(f"Time needed: {endtime - starttime} seconds")        # 9.Wyswietlam wartość różnicy czasu miedzy start a endtime żeby otrzymać wynik w sekundach
#     return wrapper1                                             # 10.Zwracam funkcje wewnętrzną
# @measuretime                                                        # 1.1.Dekorator funkcji wastetime - funkcja measuretime jest funkcją dekorującą
# def wastetime():                                                    # 1.Definicja funkcji podstawowej
#     value = sum([i**2 for i in range(1000000)])                     # 2.Liczy sume kwadratów wartości (liczb podniesionych do potęgi 2) liczb z zakresu od 0 do 1000000
#     print(value)                                                    # 3.Wyświetla wyliczoną sume przypisaną do zmiennej value
# wastetime()
# print(wastetime.__name__)
import re
#
# txt = "welcome, welcome to the jungle"  # string inside txt variable
# z = txt.split()                         # split method to return the list of words in string
# y = re.sub('welcome', 'hello', txt)     # sub method to replace the occurence of 'welcome' with 'hello', returning replaced string
# x = re.subn('welcome', 'hello', txt)    # subn method to replace the occurence of 'welcome' with 'hello', returning tuple of the replaced string with number of replaced word occurences
# print(z, type(z))                       # printing with information about type of data - List
# print(y, type(y))                       # printing with information about type of data - string
# print(x, type(x))                       # printing with information about type of data - tuple


# Return double of n
# def addition(n):
#     return n + n
# def multiply(n):
#     return n*n
#
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# result_1 = map(multiply, numbers)
# print(tuple(result))
# print(list(result_1))


# #
# def double(items):
#     output = []
#     for val in items:
#       output.append(val * 2 )
# #     return output
# #
# zmienna = lambda x,y,z : x*y*z      # Funkcja lambda przyjmuje 3 argumenty i jej zadanie to je pomnożyć przez siebie
# print(zmienna(2,3,4))               # Wyswietlamy wywołanie funkcji lambda przypisanej do zmiennej - zmienna



# def double(items):                              # Definicja funkcji podwajającej przyjetą wartość
#     return list(map(lambda x: x*x, items))      # Funkcja map wykorzystująca wyrażenie lambda oraz argument funkcji double - items
# result = double(numbers)
# print(result)

# def filter_1(items):
#     return list(filter(lambda y: y<=4, items))  # Funkcja filter wykorzystująca wyrażenie lambda oraz argument funkcji filter_1 - items
# result = filter_1(numbers)                      # Funkcja filter filtruje w tym przypadku liste z wartosci y<=4
# print(result)
#.
# from functools import reduce
# numbers = [3,4,5,1,8,4,6]
# def reduce_1(items):
#     return reduce(lambda x,y: x-y, items)       # Funkcja reduce wykorzystująca wyrażenie lambda oraz argument funkcji filter_1 - items
# result = reduce_1(numbers)                      # Funkcja reduce redukuje zbiór do jednej wartosci. W tym przypadku wzór bedzie wygladał
# print(result)                                   # tak: (((((((3-4)-5))-1)-8)-4)-6)
# import pandas as pd
#
# sheet = 1
# df = pd.read_excel(r'C:\Users\pikowals\PycharmProjects\pythonProject1\test.xlsx')   # r' to convert normal string to raw string
# print(df.head(4))

# Printing only 5 first rows
# def csv_reader(file_name):
#     file = open(file_name,encoding='cp437')
#     result = file.read().split("\n")
#     return result
# x = csv_reader('test.xlsx')
# print(x)
#
# from collections.abc import Iterable, Iterator
#
# class FibonacciIterable(Iterable):
#     def __init__(self, limit):
#         self.limit = limit
#
#     def __iter__(self):
#         return FibonacciIterator(self.limit)
#
#
# class FibonacciIterator(Iterator):
#     def __init__(self, limit):
#         self.iteration = 0
#         self.a = 0
#         self.b = 1
#         self.limit = limit
#
#     def __next__(self):
#         result = self.a
#         if self.limit < self.iteration:
#             raise StopIteration
#         self.a, self.b = self.b, self.a + self.b
#         print(self.a ,self.b)
#         self.iteration += 1
#         return result
#
# fibonacci = FibonacciIterable(10)
# for value in fibonacci:
#     print(value) # 0, 1, 1, 2, 3, 5
#
# class square:
#     def __init__(self, side_square):
#         #wnetrze klasy init
#         print("wewnątrz inita")
#         self.side_square = side_square
#
#         y = [1,2,3]                     # Lista
#         z = (2,5,7)                     # Tupla
#         x = {1:'ptak',2:'orzeł'}        # Słownik
#         print(type(x))                  # Printuje typ x'a
#         print(2 in y)                   # Wyswietla true/false (boolean) jesli w liscie y znajduje sie wartosc 2
#         print(y.__contains__(2))        # Wywołanie dunder methody __contains__ w celu sprawdzenia czy lista y zawiera wartosc 2 - zwraca boolean
#         print(z.__contains__(7))        # Wywołanie dunder methody __contains__ w celu sprawdzenia czy tupla z zawiera wartosc 7 - zwraca boolean
#         print(x.__contains__(2))        # Wywołanie dunder methody __contains__ w celu sprawdzenia czy słownik x zawiera klucz 2 - zwraca boolean
#         print(x.__getitem__(2))         # Wywołanie dunder methody __getitem__ w celu sprawdzenia co kryje sie pod kluczem 2 w słowniku x
#         print(x.__missing__())
#         print(y.__len__())
# kwadr = square(2)
# import datetime
#
#
# # def oneHundred():
# #     name = input("Give me your name: ")
# #     year = input("Give me you birth year: ")
# #     y = int(year)+100
# #     print(f"{name} you will turn 100 in: {y}")
# # oneHundred()
#
# class tempList(list):
#
#
# class wiek:
#     def __init__(self):
#         imie = input("Give me your name: ")
#         wiek = input("Give me you birth year: ")
#         copy_nr = input("Give number of coppies you want that message to be printed")
#         y = int(wiek) + 100
#         for i in range(int(copy_nr)):
#             print(f"{imie} you will turn 100 in: {y}")
# wiek_1 = wiek()





# class DictSubclass(dict):
#     def __missing__(self, key):
#         print(f"Missing {key = }")
#
# my_dict = DictSubclass()
# my_dict[0] = True
# my_dict[1] = 'New'
# my_dict[2] = 'Old'
# print(my_dict)
# if my_dict[0]:
#     print("Key 0 was `True`.")
# # Prints: Key 0 was `True`
# my_dict[3]  # Prints: Missing key = 1
# Hello, world!
# class YN:
#     def __format__(self, format_spec):
#         return "N" if "n" in format_spec else "Y"
#
# print("{:aaabbbccc}".format(YN())) # Result is 'Y'
#
# f"{YN():nope}"              # Result is 'N'


# def decorating(function):                                   # 3.Funkcja dekorująca która przyjmuje jako argument funkcje w tym przypadku bedzie to funkcja counting (patrz wywołanie ostatnie 2 linie) - rozszerza działanie funkcji podstawowej
#     def adding():                                           # 4.Definicja funkcji wewnętrznej
#         print("dodaje wartość do podstawowego liczenia")    # 5.Wyswietlanie dodatkowego wpisu - dekoracja
#         function()                                          # 6.Wywołanie funkcji z argumentu funkcji zewnętrzenej
#     return adding                                           # 7.Zwrócenie funkcji wewnętrzenej - tym sposobem wywołujemy funkcje adding
#
# @decorating
# def counting():                                             # 1.Definicja funkcji podstawowej
#     print("licze sobie coś")                                # 2.Funkcja wyswietla na ekranie wpis
# counting()                                                  # 8.Wywołanie funkcji podstawowej wraz z dekoratorem
#
