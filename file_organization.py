# import shutil, os
# os.chdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat') # podajemy sciezke na ktorej chcemy pracowac
# print(shutil.copy(r'random.txt', r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy')) # kopiujemy plik z lokalizacji z pierwszego argumentu do lokalizacji z drugiego
# print(shutil.copy(r'random.txt', r'random_1.txt')) # powyższa linijka skopiuje plik random.txt do tego samego folderu ale nada nowemu plikowi nazwe random_1.txt

# import shutil, os
# os.chdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat')
# print(shutil.copytree(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat', r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\wariat_backup'))
# # Powyższa metoda skopiuje zawartosc całego wskazanego folderu i przerzuci go do folderu wariat_backup przy okazji tworząc go
#
# import shutil, os
# print(shutil.move(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\New_Microsoft_Excel_Worksheet.xlsx', r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy'))
#
# import shutil, os
# #print(os.unlink(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\do_usuniecia\plik.txt'))
# print(shutil.rmtree(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\wariat\do_usuniecia'))
# # powyższe funkcje należy stosować bardzo ostrożnie - Zeby nie usunąć przypadkowo ważnych plików!!!

# import send2trash, os
# os.chdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1')
# baconFile = open('bacon.txt','a')
# baconFile.write('Bekon nie jest warzywem.')
# baconFile.close()
# send2trash.send2trash('bacon.txt')

# import os
# os.chdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy')
#
#
# for folderName, subfolders, filenames in os.walk(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy'):
#     print('Katalog bieżacy to ' + folderName)
#     for subfolder in subfolders:
#         print('Podkatalog Katalogu '+ folderName + ': '+ subfolder)
#
#     for filename in filenames:
#         print('Plik katalogu '+ folderName +': '+ filename)
#     print('')

# import zipfile, os
# os.chdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\jakistam\ijeszczejeden')
# exampleZip = zipfile.ZipFile('plik.zip')                                   # Metoda ZipFile uruchamia init klasy ZipFile i otwiera plik zip w pythonie
# print(exampleZip.namelist())                                               # Metoda namelist zwraca listę plików znajdującą sie w archiwum zip
# plikInfo = exampleZip.getinfo('plik.txt')                                  # getinfo pozwala pobrać informacje o pliku
# print(plikInfo.file_size)                                                  # atrubut file_size przechowuje oryginalną wielkość pliku w bajtach
# print(plikInfo.compress_size)                                              # atrybut compress_file przechowuje wielkośc pliku po kompresji
# print('Skompresowany plik jest %sx mniejszy!' % (round(plikInfo.file_size/plikInfo.compress_size,3))) # obliczanie efektywności kompresji - funkcja round pobiera 2 argumenty - drugi argument wskazuje ile miejsc po przecinku
#                                                                                                       # ma być widoczne po operacji

# import zipfile, os
# os.chdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\jakistam\ijeszczejeden')
# exampleZip = zipfile.ZipFile('ijeszczejeden.zip')
# exampleZip.extractall()     # Wypakowuje wszystkie pliki z zipa do bieżącej lokalizacji - można wskazac lokalizację docelową podajac argument
# exampleZip.extract('plik.txt', r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\jakistam') # Wypakowuje wskazany plik do podanej lokalizacji

# import zipfile,os
# os.chdir(r'C:\Users\pikowals\PycharmProjects\pythonProject1\testowy\jakistam\ijeszczejeden')
# newZip = zipfile.ZipFile('new.zip','w') # otwieramy zipa w trybie zapisu tak jak to było z plikami
# newZip.write('plik.txt', compress_type=zipfile.ZIP_DEFLATED)       # metodzie write przekazujemy plik który chcemy dodac do archiwum
# newZip.close()                                                     # podajemy też typ kompresji w tym przypadku zipfile.ZIP_DEFLATED - najbardziej popularny

##############################################################################################
"""Changing american dates to european in files"""
##############################################################################################
# import re, os, shutil
# print(os.getcwd())
# x = 'to jest data 12-04-1991 ktora musi byc zamieniona.txt'
# americanDatesRegex = re.compile(r'''(^(.*?)     # cokolwiek co znajduje sie przed datą  - znak daszka
#                                     ((0|1)?\d)
#                                     (-)
#                                     ((0|1|2|3)?\d)
#                                     (-)
#                                     ((19|20)\d\d)
#                                     (.*?)$)''', re.VERBOSE) # cokolwiek znajduje sie po dacie - znak $

# # n0 = americanDatesRegex.sub(r'''\2\6-\3-\9\11''', x) # odczytywnae jako
# # print(n0)
# file_list_for_date_change = os.listdir(r'C:\Users\Piotr\Documents\pycharm_projects\pliki')
# print(file_list_for_date_change)
# for i in file_list_for_date_change:
#     if americanDatesRegex.search(i):
#         n1 = americanDatesRegex.sub(r'''\2\6-\3-\9\11''', i)
#         n2 = shutil.move(os.path.join(r'C:\Users\Piotr\Documents\pycharm_projects\pliki', i), os.path.join(r'C:\Users\Piotr\Documents\pycharm_projects\pliki',n1))
#         print(n2)
# file_list_for_date_change_updated = os.listdir(r'C:\Users\Piotr\Documents\pycharm_projects\pliki')
# print('Nowe pliki \n', file_list_for_date_change_updated)
# for j in file_list_for_date_change_updated:
#     if americanDatesRegex.search(j):
#         m1 = americanDatesRegex.search(j)
#         group3 = m1.group(3)
#         group6 = m1.group(6)
#         if len(group3) == 1:
#             group3 = '0' + str(group3)
#         print(group3)
#         if len(group6) == 1:
#             group6 = '0' + str(group6)
#         print(group6)
#         m1 = americanDatesRegex.sub(rf'\g<2>{group3}-{group6}-\9\11', j) # grupa 3 jest pierwsza bo juz raz zamienilismy
#         print(m1)                                                        # miejscami w pierwszej pętli wiec nie ma potrzeby robić to po raz 2
#         m2 = shutil.move(os.path.join(r'C:\Users\Piotr\Documents\pycharm_projects\pliki', j), os.path.join(r'C:\Users\Piotr\Documents\pycharm_projects\pliki', m1))

##############################################################################################
"""Removing zeros from the file title"""
##############################################################################################
# import re, shutil, os
#
# tekst = 'spam0041.txt'
# removeZerosRegex = re.compile(r'''(^(.*?)
#                                     (0+)
#                                     (\d+)
#                                     (.*?)$)''', re.VERBOSE)
# m1 = removeZerosRegex.search(tekst)
# n1 = os.listdir(r'C:\Users\Piotr\Documents\pycharm_projects\pliki')
# for i in n1:
#     m2 = removeZerosRegex.sub(r'''\g<2>\g<4>\g<5>''', i)
#     m3 = shutil.move(os.path.join(r'C:\Users\Piotr\Documents\pycharm_projects\pliki', i), os.path.join(r'C:\Users\Piotr\Documents\pycharm_projects\pliki',m2))
##############################################################################################
"""Adding files to zip"""
##############################################################################################
# import zipfile, os
#
# def backupToZip(folder):
#     folder = os.path.abspath(folder)  # sprawdzamy czy argumentem jest bezwgledna scieżka dostępu do folderu
#     number = 1
#     while True:
#         zipFileName = os.path.basename(folder) + '_' +str(number) + '.zip'
#         if not os.path.exists(zipFileName):
#             break
#         number = number + 1
#     print('Tworze archiwum %s...' %(zipFileName))
#     backupZip = zipfile.ZipFile(zipFileName, 'w')
#     for foldername, subfolders, filenames in os.walk(folder):
#         print('Dodawanie plików w %s...' % (foldername))
#         backupZip.write(foldername)
#         for filename in filenames:
#             newBase = os.path.basename(folder) + '_'
#             if filename.startswith(newBase) and filename.endswith('.zip'):
#                 continue
#             backupZip.write(os.path.join(foldername,filename))
#     backupZip.close()
#     print('Gotowe!')
#
# backupToZip(r'C:\Users\Piotr\Documents\pycharm_projects\pliki')
##############################################################################################
"""Program is looking for txt and py files and add them to the zip"""
##############################################################################################
# import zipfile, os, re
# def zipPyAndTxt(folder):
#     folder = os.path.abspath(folder)
#     filesToZipRegex = re.compile(r'''(^(.*)
#                                    (\.)
#                                    (txt|py)$)''', re.VERBOSE)
#     archiwumzip = os.path.basename(folder) + '_py_txt_archive' + '.zip'
#     backupZip = zipfile.ZipFile(archiwumzip, 'w')
#     for folders, subfolders, filenames in os.walk(folder):
#         print('Dodawanie plików w %s' %(folders))
#         backupZip.write(folders)
#         for filename in filenames:
#             if filesToZipRegex.search(filename):
#                 print('Nie dodajemy plików z rozszerzeniem txt i py')
#                 continue
#             else:
#                 backupZip.write(os.path.join(folders,filename))
#     backupZip.close()
# zipPyAndTxt(r'C:\Users\Piotr\Documents\pycharm_projects\pliki')
##############################################################################################
"""Program is looking for jpegs and pdfs and copy them in one directory"""
##############################################################################################
# import re, os, shutil
#
# def pdfJpgFinder(folder):
#     pdfJpgRegex = re.compile(r'''(^(.*)
#                                    (\.)
#                                    (pdf|jpg)$)''', re.VERBOSE)
#     folder = os.path.abspath(folder)
#     for foldername, subfolders, filenames in os.walk(folder):
#         for filename in filenames:
#             if pdfJpgRegex.search(filename):
#                 #print(os.path.join(r'C:\Users\Piotr\Documents\pycharm_projects\testowy\jakistam\Nowy_folder', filename))
#                 if os.path.exists(os.path.join(r'C:\Users\Piotr\Documents\pycharm_projects\testowy\jakistam\Nowy_folder', filename)):
#                     print('Istneje plik %s - pomiń plik w przenoszeniu' %(filename))
#                     continue
#                 else:
#                     print('Dodaje plik %s jako nowy unikatowy plik' % (filename))
#                     print(os.path.join(foldername, filename))
#                     print(shutil.copy(os.path.join(foldername,filename), r'C:\Users\Piotr\Documents\pycharm_projects\testowy\jakistam\Nowy_folder'))
# pdfJpgFinder(r'C:\Users\Piotr\Documents\pycharm_projects\testowy\jakistam')
##############################################################################################
"""Program is looking for folders and files that weights more that 1700bytes"""
##############################################################################################
#! python3
# import os,shutil
#
# def bigFiles(folder):
#     folder = os.path.abspath(folder)
#     for foldername, subfolders, filenames in os.walk(folder):
#         foldersize = os.path.getsize(foldername)
#         if foldersize > 1700:
#             print('Duży folder %s ma rozmiar %s' % (foldername, os.path.getsize(foldername)))
#         for file in filenames:
#             filesize = os.path.getsize(os.path.join(foldername, file))
#             if filesize > 1700:
#                 print('Duży pliczek o nazwie %s ma wartość %s' % (file, os.path.getsize(os.path.join(foldername, file))))
#
# bigFiles(r'C:\Users\Piotr\Documents\pycharm_projects\testowy\foty')

##############################################################################################
"""Program is looking for spam prefix in txt files and arrange the files so that there
are not gaps in iteration"""
##############################################################################################
# import shutil, os ,re
#
# def prefixChanger(folder):
#     prefixRegex = re.compile(r'''(^(spam)
#                                    ((\d)*)
#                                    (\.)
#                                    (txt)$)''', re.VERBOSE)
#     iterator = 1
#     for foldername, subfoldername, filename in os.walk(folder):
#         for files in filename:
#             if prefixRegex.search(files):
#                 n1 = prefixRegex.search(files)
#                 n2 = n1.group(3)
#                 if int(n2) == iterator:
#                     print('Ok')
#                 else:
#                     if iterator < 10:
#                         m1 = prefixRegex.sub(rf'\g<2>00{iterator}\g<5>\g<6>', files)
#                         shutil.move(os.path.join(foldername,files),os.path.join(foldername,m1))
#                     elif iterator >10 and iterator <99:
#                         m1 = prefixRegex.sub(rf'\g<2>0{iterator}\g<5>\g<6>', files)
#                         shutil.move(os.path.join(foldername,files),os.path.join(foldername,m1))
#                     else:
#                         m1 = prefixRegex.sub(rf'\g<2>0{iterator}\g<5>\g<6>', files)
#                         shutil.move(os.path.join(foldername,files),os.path.join(foldername,m1))
#
#                 iterator = iterator + 1
# prefixChanger(r'C:\pycharm_projects\pliki\spam')




