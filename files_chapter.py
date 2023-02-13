import os
# o = os.path.join('usr','bin', 'spam')
# print(o)
# myFiles = ['konta.txt','informacje.csv', 'zaproszenie.docx']
# for filename in myFiles:
#     print(os.path.join('C:\\Użytkownicy\\Robert', filename))
# print(os.getcwd())
# os.chdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1')
# print(os.getcwd())

#
# import os
# os.makedirs(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat')
# import os
#
# print(os.path.abspath('.\\Scripts'))  # Funkcja zwróci ciąg tekstowy bezwględnej sciezki dostępu argumentu - łatwy sposób na konwersję względnej scieżki dostępu na bezwzględną
#
# print(os.path.isabs('.')) # Zwraca wartość True jeśli argument zawiera bezwzględną scieżke dostępu. W przypadku względnej scieżki dostępu zwrotną wartością bedzie False
#
# print(os.path.isabs(os.path.abspath('.'))) # zwraca True
#
# print(os.path.relpath('C:\\Windows','C:\\')) # os.path.relpath(scieżka, początek) zwróci ciąg tekstowy względnej scieżki dostępu zaczynajacy się od elementu wskazanego przez początek
#
# print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
# print(os.getcwd())
#
# import os
# path = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.basename(path)) # Zwróci to wszystko co zawiera sie po ostatnim ukośniku w argumencie wywołania
# print(os.path.dirname(path)) # Zwraca to wszystko co znajduje się przed ostatnim ukośnikiem w argumencie
# print(os.path.split(path))   # Wyswietla krotkę z dwoma ciągami tekstowymi - bazową i nazwą katalogu
# print(path.split(os.path.sep)) # Metoda split zwraca listę na którą składają sie poszczególne elementu scieżki dostępu. Konieczne jest przekazanie tej metodzie os.path.sep

# import os
# # os.makedirs(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy')
# print(os.path.getsize(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\plik.docx')) # zwraca wielkośc pliku w Bajtach
# print(os.listdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat'))                # zwraca listę nazw plików zawierajacych sie we wskazanej lokalizacji
#
# total_size = 0
#
# for i in os.listdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat'):
#     total_size = total_size + os.path.getsize(os.path.join(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat',i)) # W petli zliczamy wielkość wszystkich plików znajdujacych sie we wskzanej lokalizacji
# print(total_size)
# import os
# print(os.path.exists(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat')) # Zwróci True jeśli wskazany katalog lub plik istnieje
#
# print(os.path.exists(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\Nie_Istniejacy_folder'))    # Zwróci False dla nieistniejacej scieżki do katalogu lub pliku
#
# print(os.path.isdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat')) # Zwraca True dla istniejacej scieżki dostępu
#
# print(os.path.isfile(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat')) # Zwraca False jeśli wskazana scieżka prowadzi do katalagu zamiast pliku
#
# print(os.path.isdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\plik.docx'))  # Zwraca False jeśli wskazana scieżka prowadzi do pliku zamiast do katalogu
#
# print(os.path.isfile(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\plik.docx'))  # Zwraca True jestli scieżka prowadzi do pliku

# import os
# newFile = open(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\plik.txt','r',encoding='UTF-8')
# neFile_1 = open(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\panTadeusz.txt','r',encoding='UTF-8') # encoding UTF-8 pozwala na odczytanie z plików polskich znaków
# print(newFile.read())
# print(neFile_1.readlines())

# randomFile = open(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\random.txt', 'w', encoding='UTF-8') # Jeżeli plik o nazwie random.txt nie istnieje - python go utworzy - otwieramy w tryvie zapisu 'w'
# randomFile.write('Witam Szeryfa!\n')                                                                                    # Wpisujemy Witam Szeryfa - należy dodać znak nowego wiersza \n - domyslnie write nie dziala tak jak print
# #print(randomFile.write('Witam Szeryfa!\n'))                                                                            # Wartością zwrotną metody write() jest liczba zapisanych znaków z uwzględniemem znaku nowego wiersza
# randomFile.close()
# randomFile = open(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\random.txt', 'a', encoding='UTF-8') # Otwieramy plik w trybie dołączania 'a' żeby dodac tekst na końcu pliku
# randomFile.write('To nowa linia dodana własnie po wywołaniu metody open z argumentem \'a\'\n')                            # Nowa tekst
# randomFile.close()
# randomFile = open(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\random.txt', encoding='UTF-8')      # Otwieramy plik w trybie odczytu 'r' żeby wyswietlic zawartośc na ekranie za pomocą metody read()
# content = randomFile.read()
# randomFile.close()
# print(content)


# import shelve, os
# print(os.getcwd())
# shelfFile = shelve.open('mydata')
# cats = ['Zophie','Pooka','Simon']
# shelfFile['cats'] = cats
# shelfFile.close()
# shelfFile = shelve.open('mydata')
# print(type(shelfFile))
# print(shelfFile['cats'])
# shelfFile.close()
#
# shelfFile = shelve.open('mydata')
# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))
# shelfFile.close()

# import pprint
# import myCats
# cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
# pprint.pformat(cats)
# fileObj = open('myCats.py', 'w')
# fileObj.write('cats= ' +pprint.pformat(cats) + '\n')
# fileObj.close()
# print(myCats.cats)
# print(myCats.cats[0])
# print(myCats.cats[0]['name'])
#
# import random, os
# #print(os.getcwd())
# capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
#    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
#    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
#    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
#    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
#    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
#    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
#    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
#    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
#    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
#     'New Mexico': 'Santa Fe', 'New York': 'Albany',
#    'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
#    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
#    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
#    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
#    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
#     'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# for quiz in range(35):                                                                                                                                      # 35 iteracji pętli bo tyle ma być testow
#     quizFile = open('C:\\Users\\pikowals\\AppData\\Roaming\\JetBrains\\PyCharmCE2020.3\\scratches\\quizy\\capitalsquiz%s.txt' %(quiz+1),'w')                # za kazdą iteracja tworzymy plik z testem - % wstawia wartość do ciągu znakow
#     answerFile = open('C:\\Users\\pikowals\\AppData\\Roaming\\JetBrains\\PyCharmCE2020.3\\scratches\\quizy\\capitalsquiz_answers%s.txt' %(quiz+1), 'w')     # również tworzymy pliki z odpowiedziami
#     quizFile.write('Imie i nazwisko:\n\nData:\n\nKlasa:\n\n')                   # Do każdego pliku dołączamy nagłowek
#     quizFile.write((' ' * 20) +'Quiz stolic stanów (Quiz %s)' % (quiz +1))      # I opis quizu
#     quizFile.write('\n\n')                                                      # Dodajemy 2 wolne linie
#     states = list(capitals.keys())                                              # tworzymy listę kluczy o nazwie states
#     random.shuffle(states)                                                      # Przy każdej iteracji wartosci listy states beda losowo rozmieszczone
#     for questionNum in range(50):                                               # Pętla w petli - 50 iteracji bo ilosc stanów jest własnie taka
#         correctAnswer = capitals[states[questionNum]]                           # Własciwa odpowiedź - pobieramy wartość z listy o danym indeksie w petli i podstawiamy do słownika ktory zwraca wartość - poprawną
#         wrongAnswer = list(capitals.values())                                   # tworzymy liste niewłasciwych odpowiedzi - na chwile obecna zawiera ona wszystkie wartosci słownika states
#         del wrongAnswer[wrongAnswer.index(correctAnswer)]                       # usuwamy poprawną wartośc z listy - wronganswer[index(correctAnswer)]
#         wrongAnswer =random.sample(wrongAnswer,3)                               # Okrajamy liste przez wybranie losowych 3 błędnych odpowiedzi ktore pozostały na liscie
#         answerOption = wrongAnswer+[correctAnswer]                              # Do opcji odpowiedzi dodajemy 3 błedne plus 1 poprawną
#         random.shuffle(answerOption)                                            # Mieszamy wartosci żeby nie były w tym samym położeniu za każdym razem
#         quizFile.write('%s. Co jest stolicą stanu %s?\n' % (questionNum+1, states[questionNum]))        # do pliku quiz zapisujemy nr pytania i raz pytanie o konkretny stan w zależności od wartosci indeksu pętli
#         for i in range(4):                                                                              # Dokładamy kolejną pętle do przeprowadzenia iteracji po odpowiedziach
#             quizFile.write('    %s. %s\n' %('ABCD'[i], answerOption[i]))                                # Do pliku zapisujemy dużą litere od A-D oraz opcje odpowiedzi
#         quizFile.write('\n')                                                                            # Dodajemy nową linie co iterację
#         answerFile.write('%s. %s\n' % (questionNum+1,'ABCD'[answerOption.index(correctAnswer)]))        # Podobnie w pliku z odpowiedziami zapisujemy nr pytania oraz poprawną odpowiedz
#     quizFile.close()                                                                                    # Zamykamy pliki
#     answerFile.close()


# zaczytac plik tekstowy i przypisać do zmiennej
# sprawdzić w tekscie występowanie odpowiednio słów RZECZOWNIK, PRZYMIOTNIK, CZASOWNIK, PRZYSŁÓWEK
# odpowiednio pod każdy z tych wyrazów zapytać użytkownika o konkretne słowo
# Podstawić wpisane słowo
# zapisac wszystko do pliku
# wyswietlić przerobione zdanie


#
# import os
#
# toBeRead = open(r'C:\Users\pikowals\PycharmProjects\pythonProject1\replace_tekst.txt', 'r', encoding='UTF-8')
# from_file = toBeRead.read()
#
#
# splitted_into_list = from_file.split()
# print(splitted_into_list)
#
# for i in splitted_into_list:
#     if i == 'RZECZOWNIK' or i == 'RZECZOWNIK.':
#         print('Podaj rzeczownik: ')
#         rzecz = input()
#         splitted_into_list[splitted_into_list.index(i)] = rzecz
#     elif i == 'RZECZOWNIK.':
#         print('Podaj rzeczownik: ')
#         rzecz = input() + '.'
#         splitted_into_list[splitted_into_list.index(i)] = rzecz
#     elif i == 'PRZYMIOTNIK' or i == 'PRZYMIOTNIK.':
#         print('Podaj przymiotnik: ')
#         przym = input()
#         splitted_into_list[splitted_into_list.index(i)] = przym
#     elif i == 'CZASOWNIK':
#         print('Podaj czasownik: ')
#         czas = input()
#         splitted_into_list[splitted_into_list.index(i)] = czas
#     elif i == 'CZASOWNIK.':
#         print('Podaj czasownik: ')
#         czas = input() + '.'
#         splitted_into_list[splitted_into_list.index(i)] = czas
# print(splitted_into_list)
# joined = ''
# for i in splitted_into_list:
#     joined = joined + i + ' '
# print(joined)
#
# toBeWritten = open(r'C:\Users\pikowals\PycharmProjects\pythonProject1\replace_tekst.txt', 'w', encoding='UTF-8')
# toBeWritten.write(joined)

import os, re

print(os.getcwd())  # do sprawdzenia bieżącej lokalizacji
# C:\Users\pikowals\AppData\Roaming\JetBrains\PyCharmCE2020.3\scratches\quizy
file_list = os.listdir(r'C:\Users\pikowals\AppData\Roaming\JetBrains\PyCharmCE2020.3\scratches\quizy')  # Do utworzenia listy plików znajdujacych sie we wskazanym katalogu
print('Wprowadź wyrażenie regularne które chcesz znaleźć w plikach: ')
userRegex = input()                     # uzytkownik wprowadza wyrażenie regularne do wyszukania
userRegex_1 = re.compile(f'{userRegex}')   # przekazujemy wyrażenie regularne jako argument w nawiasach klamrowych {}
for i in file_list:                         # pętla do przechodzenia przez kazdy plik
    each_file = os.path.join(r'C:\Users\pikowals\AppData\Roaming\JetBrains\PyCharmCE2020.3\scratches\quizy', i) # podstawiamy nazwe pliku do sciezki aby przejsc przez kazdy plik w iteracji
    n = open(each_file, 'r')            # otwieramy każdy plik
    n1 = n.readlines()                  # zaczytujemy wiersze kazdego pliku - w formie listy
    for j in n1:                        # pętla na wierszach kazdego pliku
        if userRegex_1.search(j):       # sprawdzamy czy kazdy wiersz zawiera wyrażenie regularne
            print(each_file)            # wyswietlamy nazwe pliku
            print(j)                    # oraz wiersz zawierajacy wyrażenie wskazane przez uzytkownika

# otwieramy wszystkie pliki znajdujace się w lokalizacji
# przeszukujemy wiersze każdego pliku pod kątem dopasowania tego co wprowadził użytkownik
# wyswietlamy wynik