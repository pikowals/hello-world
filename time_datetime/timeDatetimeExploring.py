# import time,datetime
#
# print(time.time()) # Funkcja time zwraca liczbe sekud które upłynęły od początku epoki systemy UNIX (od 1 stycznia 1970)
import datetime
# import time
# def calcProd():
#     product = 1
#     for i in range(1,100000):
#         product = product*i
#     return product
# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('Wynik składa się z %s cyfr.' % (len(str(prod))))
# print('Wykonanie kodu zabrało %s sekund.' % (endTime-startTime))
# import time
# for i in range(3):
#     print('tick')
#     time.sleep(1)
#     print('tock')
#     time.sleep(1)

# import time
# now = time.time()
# print(round(now,2))
# print(round(now,4))
# print(round(now))

# import time
# print('Naciśnij Enter aby rozpocząć. Kolejne naciśnięcie Enter oznacza nowe okrążanie')
# print('Naciśniecie Ctrl+C kończy działanie programu.')
# input()
# print('Rozpoczęto działanie')
# startTime = time.time()
# lastTime = startTime
# lapNum = 1
# try:
#     while True:
#         input()
#         lapTime = round(time.time() - lastTime,2)
#         totalTime = round(time.time() -startTime,2)
#         print('Okrążenie #%s: %s (%s)' % (lapNum,totalTime,lapTime),end='')
#         lapNum+=1
#         lastTime =time.time()
# except KeyboardInterrupt:
#     print('\nGotowe!')

# import datetime, time
# print(datetime.datetime.now()) # zwraca bieżąca datę i godzinę
#
# dt = datetime.datetime(2015,10,21,16,29,0) # wskazanie daty i godziny
# print(dt.year,dt.month,dt.day)             # pobranie odpowiednich danych ze zmiennej dt
# print(dt.hour,dt.minute,dt.second)
#
# print(datetime.datetime.fromtimestamp(1000000)) # czas po upływie miliona sekund od poczatku epoki systemu UNIX
# print(datetime.datetime.fromtimestamp(time.time())) #  Aktualny moment

# import datetime, time
# halloween2015 = datetime.datetime(2015,10,31,0,0,0)
# newyear2016 = datetime.datetime(2016,1,1,0,0,0)
# oct31_2015 = datetime.datetime(2015,10,31,0,0,0)
# print(halloween2015==oct31_2015)
# print(halloween2015>newyear2016)
# print(newyear2016>halloween2015)
# print(newyear2016!=oct31_2015)
# import datetime
# delta = datetime.timedelta(days=11,hours=10,minutes=9,seconds=8)
# print(delta.days,delta.seconds,delta.microseconds)
# print(delta.total_seconds())
# print(str(delta))

# import datetime
# dt =datetime.datetime.now()
# print(dt)
# thousandDays = datetime.timedelta(days=1000)
# print(dt+thousandDays)

# import datetime
# oct21st = datetime.datetime(2015,10,21,16,29,0)
# aboutThirtyYears = datetime.timedelta(days=365*30)
# print(oct21st)
# print(oct21st -aboutThirtyYears)
# print(oct21st -(2*aboutThirtyYears))

# import datetime, time
# halloween2016 = datetime.datetime(2016,10,31,0,0,0)
# while datetime.datetime.now() < halloween2016:
#     time.sleep(1)

# import datetime
# oct21st = datetime.datetime(2015,10,21,16,29,0)
# print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
# print(oct21st.strftime('%I:%M %p'))
# print(oct21st.strftime("%B '%y"))
#
# import datetime
# print(datetime.datetime.strptime('21 October 2015','%d %B %Y'))
# print(datetime.datetime.strptime('2015/10/21 16:29:00','%Y/%m/%d %H:%M:%S'))
# print(datetime.datetime.strptime("October '15","%B '%y"))
# print(datetime.datetime.strptime("November '63","%B '%y"))
# import time
# iter = 0
# startTime = datetime.datetime(2023,2,26,11,42,0)  # podajemy dokładną godzinę startu
# while True:
#     while datetime.datetime.now() < startTime:
#         time.sleep(1)
#     print('Program zostanie uruchomiony co minute 3 razy.')
#     startTime = startTime + datetime.timedelta(minutes=1) # do czasu startu zostanie dodana minuta
#     print('Kolejne uruchomienie o godzinie: %s' %startTime)
#     iter += 1
#     if iter == 3:
#         break

# import threading, time, datetime
# print('Uruchomienie programu')
# def takeNap():
#     time.sleep(5)
#     print('Obudź się!')
# thredObj = threading.Thread(target=takeNap)
# thredObj.start()
# time.sleep(1)
# print('Odpalamy drugi wątek %s' % datetime.datetime.now())
# thredObj1 = threading.Thread(target=takeNap)
# thredObj1.start()
# print('Zakończenie programu.')

# import threading
# listAnim = ['Koty','Psy','Żaby']
# print('Koty','Psy','Żaby', sep=' & ') # sep = to separator miedzy kolejnymi stringami do wyswietlenia
#
# threadObj = threading.Thread(target=print, args=['Koty','Psy','Żaby'],kwargs={'sep':' & '})
# threadObj.start()

# import threading
# threadObj = threading.Thread(target=print('Koty','Psy','Żaby', sep=' & '))
# import requests, os, bs4, threading
# os.makedirs('xkcd', exist_ok=True) # Komiksy są przechowywane w katalogu ./xkcd.
#
# def downloadXkcd(startComic, endComic):
#     for urlNumber in range(startComic, endComic):
#         # Pobranie strony.
#         print('Pobranie strony http://xkcd.com/%s...' % (urlNumber))
#         res = requests.get('http://xkcd.com/%s' % (urlNumber))
#         res.raise_for_status()
#
#         soup = bs4.BeautifulSoup(res.text)
#
#         # Ustalenie adresu URL pliku obrazu komiksu.
#         comicElem = soup.select('#comic img')
#         if comicElem == []:
#             print('Nie udało się odnaleźć pliku obrazu komiksu.')
#         else:
#             comicUrl = 'http:' + comicElem[0].get('src')
#             # Pobranie obrazu.
#             print('Pobranie obrazu %s...' % (comicUrl))
#             res = requests.get(comicUrl)
#             res.raise_for_status()
#
#             # Zapis obrazu w katalogu ./xkcd.
#             imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
#             for chunk in res.iter_content(100000):
#                 imageFile.write(chunk)
#             imageFile.close()
#
# # Utworzenie i uruchomienie obiektów Thread.
# downloadThreads = [] # Lista wszystkich obiektów Thread.
# for i in range(0, 1400, 100): # Iteracja 14 razy, co powoduje utworzenie 14 wątków.
#     downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
#     downloadThreads.append(downloadThread)
#     downloadThread.start()
#
# # Zaczekanie na zakończenie działania wszystkich wątków.
# for downloadThread in downloadThreads:
#     downloadThread.join()
# print('Gotowe!')


# import subprocess, time
# calcProc = subprocess.Popen(r'C:\Windows\WinSxS\wow64_microsoft-windows-calc_31bf3856ad364e35_10.0.19041.1_none_6a03b910ee7a4073\calc.exe')
# print(calcProc.poll() == None)
#
# print(calcProc.poll())
# print(calcProc.poll())
#
# import subprocess#
# notepadProc = subprocess.Popen([r'C:\Windows\System32\notepad.exe',r'C:\Users\pkowalski7\Documents\hello.txt'])
# import subprocess
# fileObj = open('hello.txt','w')
# fileObj.write('Witaj Świecie')
# fileObj.close()
# subprocess.Popen(['start','hello.txt'], shell=True)

# import time,subprocess
#
# timeLeft = 10
# while timeLeft > 0:
#     print('Timeleft : %s' %timeLeft)
#     time.sleep(0.5)
#     timeLeft = timeLeft - 1
# subprocess.Popen(['start','alarm.wav'], shell=True)

import time,
print('Naciśnij Enter aby rozpocząć. Kolejne naciśnięcie Enter oznacza nowe okrążanie')
print('Naciśniecie Ctrl+C kończy działanie programu.')
input()
print('Rozpoczęto działanie')
startTime = time.time()
lastTime = startTime
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time() -startTime,2)
        print('Okrążenie #%s:  %s (  %s)' % (str(lapNum).rjust(2),str(round(totalTime,2)).rjust(6),str(f'{lapTime:.2f}').rjust(3)),end='')
        lapNum+=1
        lastTime =time.time()
except KeyboardInterrupt:
    print('\nGotowe!')

