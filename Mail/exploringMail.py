# import smtplib
# smtpObj = smtplib.SMTP('smtp.gmail.com',587) # połaczenie z serwerem poczty gmail / port 587 oznacza szyfrowanie TLS
# print(type(smtpObj))
# print(smtpObj.ehlo())   # funkcja ehlo to przywitanie z serwerem - wartość zwrotna 250 oznacza sukces
# print(smtpObj.starttls()) # funkcja starttls włącza szyfrowanie połączenia jako że używamy portu 587,
#                           # Jeśli używamy portu 465 to znaczy że używamy szyfrowania SSL wiec wywolanie starttls jest niepotrzebne
# print(smtpObj.login('januszkowalski900000@gmail.com','zmzevpiiextxintr'))
# print(smtpObj.sendmail('januszkowalski900000@gmail.com','p.kowal26@gmail.com','Subject: Tak długo...\nDrogi Piotrze\nPozdrawiam,\nPiotr'.encode('UTF-8')))

# import pyzmail, imapclient, pprint, datetime, imaplib
# imaplib._MAXLINE = 10000000
# imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)         # Nawiązywanie połączenia z serwerem gmail - imap.gmail.com
# print(imapObj.login('januszkowalski900000@gmail.com','zmzevpiiextxintr'))   # Używamy loginu i hasła wygenerowanego wczesniej w weryfukacji dwuetapowej
# # pprint.pprint(imapObj.list_folders())
# imapObj.select_folder('INBOX',readonly=True)
# mails = imapObj.search(['ALL'])                                 # Wyszukiwanie wszystkich maili w folderze
# print(mails)
# mails2 = imapObj.search(['ON', datetime.datetime(2023,2,27)])  # Wyszukanie maili wysłanych w określonej dacie
# print(mails2)
# mails3 = imapObj.search(['SINCE', datetime.datetime(2023,2,27), 'UNSEEN']) # Maile wysłane od 27- lutego 2023 które są nieodczytane
# print(mails3)
# mails4 = imapObj.search(['SINCE', datetime.datetime(2023,2,27), 'FROM', "p.kowal26@gmail.com"]) # Maile wysłane od 27 lutego 2023 przez p.kowal26@gmail.com
# print(mails4)
# mails5 = imapObj.search(['SINCE', datetime.datetime(2023,2,27), 'NOT','FROM', "p.kowal26@gmail.com"]) # Maile wysłane od 27 lutego 2023 NIE przez p.kowal26@gmail.com
# print(mails5)
# maile_gmail = imapObj.gmail_search('kowalski')      # Bardzo zaawansowany silnik do przeszukiwania poczty gmail
# print(maile_gmail)
# imapObj.select_folder('INBOX',readonly=False)
# rawMessages = imapObj.fetch(maile_gmail,['BODY[]'])
# pprint.pprint(rawMessages)
# message = pyzmail.PyzMessage.factory(rawMessages[8][b'BODY[]'])  # użycie b'BODY[]' jest potrzebne - samo BODY[] nie działa
# print(message)
# print(message.get_subject(),'<---- To jest tytuł maila')
# print(message.get_addresses('from'), '<---- To jest nadawca')
# print(message.get_addresses('to'),'<---- To jest odbiorca')
# print(message.get_addresses('cc'))
# print(message.get_addresses('bcc'))
# print(message.text_part != None)
# print(message.text_part.get_payload().decode(message.text_part.charset))
# print(message.html_part != None)
# print(message.html_part.get_payload().decode(message.text_part.charset))
#
# print(imapObj.delete_messages(maile_gmail))
# print(imapObj.expunge())
# print(imapObj.logout())

####################################################################################
####################################################################################
#Projekt wysyłanie wiadomości e-mail z przypomnieniami o składkach
####################################################################################
####################################################################################

# import openpyxl,smtplib,sys
# wb = openpyxl.load_workbook('duesRecords.xlsx')
# sheet = wb.active # lub wb['Sheet1']
# print(sheet)
# lastCol = sheet.max_column
# latestMonth = sheet.cell(row=1, column=lastCol).value
#
# print(lastCol, latestMonth)
# unpaidMembers = {}
# for r in range(2, sheet.max_row):
#     payment = sheet.cell(row=r,column=lastCol).value
#     if payment!='zapłacono':
#         name = sheet.cell(row=r,column=1).value
#         email= sheet.cell(row=r,column=2).value
#         unpaidMembers[name] = email
# print(unpaidMembers)
# smptObj = smtplib.SMTP('smtp.gmail.com',587)
# smptObj.ehlo()
# smptObj.starttls()
# print(smptObj.login('januszkowalski900000@gmail.com','zmzevpiiextxintr'))
# for name, email in unpaidMembers.items():
#     print('Wysyłanie wiadomości e-mail na adres %s ...' % email)
#     sendmailStatus = smptObj.sendmail('januszkowalski900000@gmail.com', email, f'Subject: Zaległa składka za {latestMonth}.\nWitaj, {name}!\nPrawdopodobnie masz niezapłaconą składkę za miesiac {latestMonth}. Proszę o jak najszybsze uregulowanie należności.\nDziękuje!'.encode('utf-8'))
#     if sendmailStatus != {}:
#         print('Wystąpił problem podczas wysyłania wiadomości e-mail an adres %s: %s' %(email,sendmailStatus))
# smptObj.quit()

# import random, openpyxl, smtplib, datetime
# def taskAssigner():
#     tasks = ['pozmywać naczynia','posprzątać łazienkę','odkurzyć dom','wyprowadzić psa','wynieść śmieci','podlać kwiatki']
#     wb = openpyxl.load_workbook('maile.xlsx')
#     sheet = wb.active
#     smptObj = smtplib.SMTP('smtp.gmail.com',587)
#     smptObj.ehlo()
#     smptObj.starttls()
#     print(smptObj.login('januszkowalski900000@gmail.com','zmzevpiiextxintr'))
#     prevTaskList = {'alicja@example.com': 'podlać kwiatki', 'p.kowal26@gmail.com': 'posprzątać łazienkę', 'karol@example.com': 'odkurzyć dom', 'dawid@example.com': 'wyprowadzić psa', 'ewa@example.com': 'pozmywać naczynia', 'fred@example.com': 'wynieść śmieci'}
#     taskList = {}
#     for i in range(2,sheet.max_row+1):
#         personMail = sheet.cell(row=i,column=1).value
#         while True:
#             assignedTask = random.choice(tasks)
#             taskList[personMail] = assignedTask
#             if taskList[personMail] == prevTaskList[personMail]: # infinite loop dla przypadku gdy fred dostaje to samo zadanie co poprzednio bo jest ostatni w kolejce
#                 print('Zadanie sie powtarza dla %s' % personMail)
#                 if i == sheet.max_row:
#                     i = 2                                           # Omijamy przez kolejny warunek przy ostatnim mailu
#                     print('trafilismy infinit loop, powtarzamy pętle!')
#                     break
#                 continue
#             else:
#                 tasks.remove(assignedTask)
#                 smptObj.sendmail('januszkowalski900000@gmail.com', personMail,f'Subject: {assignedTask}'.encode('UTF-8'))
#                 break
#     print(taskList)
# startTime = datetime.datetime(2023,2,28,16,18,0)        # Start uruchamiania programu
# # taskAssigner()
# while True:
#     if datetime.datetime.now() > startTime:
#         taskAssigner()
#         startTime = startTime + datetime.timedelta(minutes=1)
#     if datetime.datetime.now() > datetime.datetime(2023,2,28,16,20,0): # konczymy uruchamianie programu po 2 minutach (3 razy wykona się petla)
#         break
#
import subprocess,
from PIL import ImageColor

subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE')