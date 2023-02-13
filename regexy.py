# def isPhonenumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False
#     return True

# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhonenumber(chunk):
#         print("Namierzono numer telefonu: " + chunk)
# print('Gotowe')

# import re
# message = 'Zadzwoń pod numer 415-555-1011 po przerwie.415-555-9999 to moje biuro.'
# message_1 = 'Zadzwoń pod numer 555-1011 po przerwie.555-9999 to moje biuro.'
#
# phoneNumRegEx = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # niezmodyfikowany ciąg tekstowy z użyciem literki r'| Funkcja compile przekazuje żądany wzorzec i umieszczamy wzorzec regex w zmiennej phonenumregex
# mo = phoneNumRegEx.search(message)                    # Wywołujemy meotde search na regexie i jako argument podajemy ciąg tekstowy który bedzie przeszukany pod kątem dopasowania - wynik podstawiamy do mo
# print(mo.group())      # W przykładzie wiemy ze dopasowanie zostanie znalezione wiec wiemy że mo zawiera obiekt Match a nie wartość NULL, wiec mozemy wywołać metode group
# m1 = phoneNumRegEx.search(message_1)
# print(m1.group())
# import re
# heroRegex = re.compile(r'Batman|Tina Fey')  # | Jest nazywany potokiem - wykorzystujemy gdy trzeba dopasować jedno z wielu wyrażen
# mo1 = heroRegex.search('Batman i Tina Fey')
# print(mo1.group())
# mo2 = heroRegex.search('Tina Fey i Batman')
# print(mo2.group())

# import re
# batRegex = re.compile(r'Bat(wo)+man') # Fragment (wo)? wyrażenia regularnego oznacza że wzorzec wo jest grupą opcjonalną
# mo = batRegex.search('The Adventures of Batman')
# print(mo.group())
# m1 = batRegex.search('The Adentures of Batwoman')
# print(m1.group())
# m2 = batRegex.search('The Adventure of Batwowowowoman')
# print(m2.group(0))
# print(m2.group(1))
# import re
# greedyhaRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyhaRegex.search('HaHaHaHaHa')
# nongreedyhaRegex = re.compile(r'(Ha){3,}')
# mo2 = nongreedyhaRegex.findall('HaHaHaHaHa HaHaHa')
# print(mo1.group())
# print(mo2)

# import re
# message = 'Zadzwoń pod numer 415-555-1011 po przerwie.415-555-9999 to moje biuro.'
# message_1 = 'Zadzwoń pod numer 555-1011 po przerwie.555-9999 to moje biuro.'
#
# phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegEx.search(message)
# print(mo.group())
#
# phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #BRAK GRUP
# m1 = phoneNumRegEx.findall(message)
# print(m1)
#
# phoneNumRegEx = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #Zdefiniowane grupy
# m1 = phoneNumRegEx.findall(message)
# print(m1)

# import re
# xmasRegex = re.compile(r'\d+\s\w+')
# # Wyrażenie regularne \d+\s\w+ dopasuje tekst zawierajacy jedna cyfrę bądź wiecej cyfr (\d+), po któryhc znajduje się spacja, tabulator
# # lub znak nowego wiersza (\s) a dalej jeden znak lub wiecej znaków słowa (\w+), takich jak cyfry i znaki podkreślenia. Metoda Findall zwróci listę
# # składającą się ze wszystkich dopasowań ciągow tekstowych
# store = '12 drummer, 11 pipers, 10 lords, 9 ladiers, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
# m3 = xmasRegex.findall(store)
# print(m3)

# import re
# vowelRegex = re.compile(r'[^aeiouAEIOU]')
# n0 = vowelRegex.findall('RoboCop je pokarm dla dzieci. POKARM DLA DZIECI')
# print(n0)
# import re
# beginsWithHello = re.compile(r'^Witaj')
# n0 = beginsWithHello.search('Witaj, Swiecie!')
# print(n0)
# n1 = beginsWithHello.search('Powiedział witaj.')
# print(n1)

# import re
# endsWithNumber = re.compile(r'\d$')
# b0 = endsWithNumber.search('Twój numer to 42')
# print(b0)
# b1 = endsWithNumber.search('Twój numer to czterdzieści dwa.')
# print(b1)

# import re
# wholeStringIsNum = re.compile(r'^\d+$')         # Wyrażenie r'^\d+$' dopasowuje ciąg tekstowy który zarówno rozpoczyna się i konczy jedną cyfrą lub wiekszą liczbą cyfr
# v0 = wholeStringIsNum.search('1234567890')
# print(v0)
# v1 = wholeStringIsNum.search('01234xyz56789')   # Konieczne jest dopasowanie całego ciągu tekstowego
# print(v1)
# v2 = wholeStringIsNum.search('01234 56789')     # Konieczne jest dopasowanie całego ciagu tekstowego
# print(v2)

# import re
# atRegex = re.compile(r'.ba')   # Dopasowuje dokładnie jeden znak oprócz znaku nowej linii
# c0 = atRegex.findall('Baba bada baobaby. Baba dba o oba baobaby.')
# print(c0)

# import re
# nameRegex = re.compile(r'Imie: (.*?) Nazwisko: (.*?)') # znak (.*) oznacza dopasuj cokolwiek
# mo = nameRegex.search('Imie: Piotr   Nazwisko: Kowalski') # białe znaki nie maja tu znaczenia
# print(mo.group())
# print(mo.group(1))
# print(mo.group(2))

# import re
# nongreedyRegex = re.compile(r'<.*?>') # Wersja niezachłanna
# m0 = nongreedyRegex.search('<To jest obsługa> w restauracji.>')
# print(m0.group())
# greedyRegex = re.compile(r'<.*>')     # Wersja zachłanna
# m1 = greedyRegex.search('<To jest obsługa> w restauracji.>')
# print(m1.group())
# import re
# noNewLineRegex = re.compile('.*')       # Działa dla wszystkich znaków z pominięciem znaku nowej linii
# m0 = noNewLineRegex.search('Służyć spoleczeństwu.\nChronić niewinnych.\nStać na straży prawa.')
# print(m0.group())
# newLineRegex = re.compile('.*', re.DOTALL) # Użycie drugiego argumentu re.DOTALL sprawia że kropa bedzie dopasowywała wszystkie znaki łącznie ze znakami nowego wiersza
# m2 = newLineRegex.search('Służyć spoleczeństwu.\nChronić niewinnych.\nStać na straży prawa.')
# print(m2.group())
#
# import re
# robocop = re.compile(r'robocop', re.I)     # Drugi argument do ignorowania wielokości liter
# n0 = robocop.search('Robocop to po części człowiek i maszyna, ale w całości glina')
# print(n0.group())
#
# n1 = robocop.search('ROBOCOP chroni niewinnych')    # Działa w kazdym przykładzie
# print(n1.group())
#
# n2 = robocop.search('Duzo postaci Robocop w książce')
# print(n2.group())

# import re
# namesRegex = re.compile(r'Agent (\w)\w+')
# n0 = namesRegex.sub(r'\1****', 'Agent Alicja powiedziała Agent Karolinie, że Agent Ewa wiedziała o podwójnej roli Agent Beaty.')
# print(n0)

# import re
# phoneRegex = re.compile(r'''(
#                             (\d{3}|\(\d{3}\))?           # Numer kierunkowy
#                             (\s|-|\.)?                   # Separator
#                             \d{3}                        # Pierwsze 3 cyfry
#                             (\s|-|\.)                    # Separator
#                             \d{4}                        # 4 kolejne cyfry
#                             (\s*(ext|x|ext.)\s*\d{2,5})? # Numer wewnętrzny
#                             )''', re.VERBOSE)

# import re
# someRegexText = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
# import re
# emailRegex = re.compile(r'''(
#                             [a-zA-Z0-9.%+-]+
#                             @
#                             [a-zA-Z0-9.-]+
#                             (\.[a-zA-Z]{2,4})
#                             )''', re.VERBOSE)

#! python3

# import re, pyperclip
# phoneRegex = re.compile(r'''(
#                             (\d{3}|\(\d{3}\))?           # Numer kierunkowy
#                             (\s|-|\.)?                   # Separator
#                             \d{3}                        # Pierwsze 3 cyfry
#                             (\s|-|\.)                    # Separator
#                             \d{4}                        # 4 kolejne cyfry
#                             (\s*(ext|x|ext.)\s*\d{2,5})? # Numer wewnętrzny
#                             )''', re.VERBOSE)
#
# emailRegex = re.compile(r'''(
#                             [a-zA-Z0-9.%+-]+             # Nazwa użytkownika
#                             @                            # Małpa
#                             [a-zA-Z0-9.-]+               # Nazwa domeny
#                             (\.[a-zA-Z]{2,4})            # kropka i poźniej cokolwiek
#                             )''', re.VERBOSE)
# data = str(pyperclip.paste())
# trafienia = []
# n0 = phoneRegex.findall(data)  # Metoda findall zwraca listę nie powtarzających się trafien
#                                # Jesli mamy wiecej niż jedną grupe metoda zwróci listę tupli
# for i in n0:
#     trafienia.append(i[0])     # Pierwsze elementy każdej tupli
# dotChange = re.compile(r'\.+') # Tworze regex do wyszukiwania 1 lub wiecej kropek
# x = 0
# for i in trafienia:
#     trafienia[x]= dotChange.sub('-', i) # w pętli podmieniam każdą kropke na myślinik w wartosciach na liscie trafienia i przypisuje jako nową wartość
#     x+=1
# for i in emailRegex.findall(data):
#     trafienia.append(i[0])              # Rozszerzamy liste trafenia o nowe wartosci znalezione przez metode findall
#                                         # Warto zaznaczyć ze metoda zwraca liste tupli (ilosc tupli zalezy od grup wyrażenia regularnego)
#                                         # dlatego podstawiamy zawsze 0 indeks tupli ktory przechowuje pełne dopasowanie
#                                         # Dla przypomnienia:
#                                         # listTuple = [(1,2,3,4),(4,3,2,1)]
#                                         # for i in listTuple:
#                                         # print(i[0])
# if len(trafienia)>0:
#     pyperclip.copy('\n'.join(trafienia)) # Kopiujemy wszystkie wartosci do schowka przy okazji łącząc je znakiem nowego wiersza
#     print('\n'.join(trafienia))          # Printujemy to co jest obecnie w schowku
#     print('Wszystkie numery telefonów oraz maile skopiowane do schowka!')
# else:
#     print('Nie znaleziono numerow telefonu ani maili')


# import re, pyperclip
#
# httpRegex = re.compile(r'''(
#                             (http|https)
#                             :{1}
#                             /{2}
#                             [a-zA-Z0-9_.,/!#$%&@()+-]+
#                             )''', re.VERBOSE)
#
# # http://dskj18e322knskwjeoimsaj ados tiasnabfwq iwqiwqsndw qwhjwqewq ndqwn https://askj120fsk sadsas https://%$@31ds43 - ciąg do skopiowania
# text = str(pyperclip.paste())
#
# matches = []
# for i in httpRegex.findall(text):
#     matches.append(i[0])
# if len(matches) > 0:
#     print('\n'.join(matches))
#     pyperclip.copy(('\n'.join(matches)))

# import re
# datesRegex = re.compile(r'''(
#                              (\d{1,4})
#                              (-|/|.)
#                              (\d{1,2})
#                              (-|/|.)
#                              (\d{1,4})
#                              )''', re.VERBOSE)
#
# text = '4-03-2017 oraz daty typu 3/01/2015 czy też 2019/6/22 lub 1-01-2000'   # Przykładowy tekst do wyłuskania dat
# matches = []
# n0 = datesRegex.findall(text)
# # for i in n0:
# #     matches.append(i[0])
# #     print(i)
#
# for i in n0:
#     if len(i[5]) == 4:
#         matches.append('-'.join([i[3],i[1],i[5]]))
#     else:
#         matches.append('-'.join([i[5],i[3],i[1]]))
#
# zeroAddRegex = re.compile(r'(\-)(\d){1}(\-)')
# x = 0
# print('Wyszukane date to: ')
# for i in matches:
#     matches[x] = zeroAddRegex.sub(r'-0\2-', i)
#     print(matches[x])
#     x+=1
# print('Natomiast po uszeregowaniu wygląda to tak:')
# matches.sort()
# for i in matches:
#     print(i)
#
# import re
#
# creditCardRegex = re.compile(r'''((\d){4}
#                                     (\s?)
#                                   (\d){4}
#                                     (\s?)
#                                   (\d){4}
#                                     (\s?)
#                                   (\d){4}
#                                     )''', re.VERBOSE)
#
# idNumber = re.compile(r'''( \s
#                             (\d{2})
#                             (\d{9}))
#                             ''', re.VERBOSE)
#
# text = 'Nr karty kredytowej odbiorcy to 0102032104320221 lub 0102 0321 0432 0221 a pesel to 91042610999'
#
# n0 = creditCardRegex.sub('#### Numer karty ukryty ####', text)
# n1 = idNumber.sub(r' \2*****', n0)
# print(n1)

# import re
#
# eliminatespacesRegex = re.compile(r'''(\s){2,}''')
# eliminateRepRegex = re.compile(r'''(!{2,})''')
# # eliminateDoubleWordsRegex = re.compile(r'''\b(\w+)(?:\W+\1\b)+''')
# eliminateDoubleWordsRegex = re.compile(r'''\b(\w+)( \1\b)+''') # \b Note that formally, \b is defined as the boundary between a \w and a \W character (or vice versa), or between \w and the beginning/end of the string.
#                                                                # This means that r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
#                                                                # Innymi słowy \b określa granice słów a \1 określa pierwszą grupe, w tym przypadku pierwszą grupą w nawiasie jest (\w+)
#                                                                # Wiec jeśli powtórzy się przynajmniej raz to samo słowo co w grupie pierwszej - regex powinien to wyłapać
#
# text = 'Witam to jest  tekst który który bedzie sprawdzany      pod kątem poprawności!!!!!!! Ciekawe czy czy zadziała!!! Ogólnie   powinien dobrze  dobrze działać!!!'
#
# n0 = eliminatespacesRegex.sub(r' ', text)
# n1 = eliminateRepRegex.sub(r'!', n0)
# n2 = eliminateDoubleWordsRegex.sub(r'\1', n1)
#
# print(n0)
# print(n1)
# print(n2)

# import re
# #
# def passStrenght():
#     print('Wprowadź hasło do sprawdzenia: ')
#     passw = input()
#     #passw = 'ABBBEEBa78' #'pierwsz drug *kdsh1@4%8dw 77777777 sajhjeq_  -Ask1&^%#@!da23 sah ABCDEFGH'
#     passLengthRegex = re.compile(r'''([a-zA-Z0-9!@#$%^&*:;,._+=-]{8,})''')  # (r'''([a-zA-Z0-9!@#$%^&*:;,._+=-]{8,})''')
#     lettersCheckRegex = re.compile(r'''(?=[a-z]+)''')    # positive lookahead assertion - sprawdzanie czy znak znajduje sie w regexie
#     lettersCheckRegex_1 = re.compile(r'''(?=[A-Z]+)''')  # Wiecej bardziej szczegółowych informacji mozna znaleźć tutaj https://www.rexegg.com/regex-lookarounds.html
#     numberCheckRegex = re.compile(r'''(?=[0-9]+)''')
#     if passLengthRegex.search(passw):
#         print('Hasło ma minumum 8 znaków')
#         if lettersCheckRegex.search(passw):
#             print('Hasło posiada małe litery')
#             if lettersCheckRegex_1.search(passw):
#                 print('Hasło posiada duże litery')
#                 if numberCheckRegex.search(passw):
#                     print('Hasło posiada przynajmniej jedną cyfre')
#                 else:
#                     print('Hasło nie posiada cyfr')
#             else:
#                 print('Hasło niema dużych liter')
#         else:
#             print('Hasło niema małych liter')
#     else:
#         print('Hasło niema 8 znaków')
#
# passStrenght()

import re
tekst = '    cos tam   '
def stripMethod(text, info = ' '):
    if info == ' ':
        removeSpacesRegex = re.compile(r'''(\A(\s)+|(\s)+\Z)''')
        n0 = removeSpacesRegex.subn('', text, count=0)
    # result = re.subn(r'''(\A(\s)+|(\s)+\Z)''','',text)
        print(n0[0])
        print(len(n0))
    else:
        # passedChares = []
        # for i in info:
        #     passedChares.append(i)
        # print(passedChares)
        charsToBeRemoved = re.compile(f'[{info}]+')
        n1 = charsToBeRemoved.sub('', text)
        print(n1)

stripMethod(tekst,'stm')