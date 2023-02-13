#! python3
#phoneAndEmail.py  - Wyszukuje numery telefonow i adresy email w schowku
#
# import pyperclip, re
#
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?                                 #Dopasowanie numeru kierunkowego
#     (\s|-|\.)?                                          #Separator
#     (\s{3})                                             #Pierwsze 3 cyfry
#     (\s|-|\.)                                           #Separator
#     (\d{4})                                             #Ostatnie 4 cyfry
#     (\s*(ext|x|ext.)|\s*(\d{2,5}))?                     #Numer wewnętrzny
#     )''', re.VERBOSE)                                   #Verbose jako pozwolenie na dodawanie komentarzy w wyrażeniach regularnych i przejrzysty kod
#
# #Wyrażenie regularne dopasowujące adres email
#
# emailRegex = re.compile(r'''(
#     [a-zA-Z0-9._%+-]+
#     @
#     [a-zA-Z0-9.-]+
#     (\.[a-zA-Z]{2,4})
#     )''', re.VERBOSE)
#
# text = str(pyperclip.paste())
# matches = []
# for groups in phoneRegex.findall(text):
#     phoneNum = '-'.join([groups[1], groups[3],groups[5]])
#     if groups[8] != '':
#         phoneNum += ' x' + groups[8]
#     matches.append(phoneNum)
# for groups in emailRegex.findall(text):
#     matches.append(groups[0])
#
# if len(matches) > 0:
#     pyperclip.copy('\n'.join(matches))
#     print('Skopiowano do schowka: ')
#     print('\n'.join(matches))
# else:
#     print('Nie znaleziono żadnego numeru telefonu lub adresu e-mail.')

import webbrowser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#webbrowser.open('https://10.44.64.85/', new=2)

# driver = webdriver.Chrome('C:/Users/pikowals/Downloads/chromedriver_win32/chromedriver.exe')
# url = "https://10.44.76.53/"
# driver.get(url)
# # button = driver.find_element_by_class_name("secondary-button")
# # button.click()


from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


url='https://10.44.92.84/'
url1='https://10.44.92.85/'

def LogIn(url):
    s = Service('C:/Users/pikowals/Downloads/chromedriver_win32/chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.get(url)
    time.sleep(15)
    return 0


LogIn(url)
LogIn(url1)

# delay = 15
# #while(True):
#
#
# button = browser.find_element("id", "details-button")
# button.click()
# button1 = browser.find_element("id", "proceed-link")
# button1.click()
# time.sleep(3)
# log = browser.find_element("id", "login-username")
# log.send_keys("Nemuadmin")
# passw = browser.find_element("id", "login-password")
# passw.send_keys("nemuuser")
# button2 = browser.find_element(By.XPATH, "/html/body/login-root/div/login/div/div/div/div[1]/form/div[3]/p-button/button/span")
# button2.click()
# time.sleep(15)
# button3 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/ui-modal-renderer/login-banner-modal/ui-modal/div/div/div[3]/div/ui-footer/div/ui-button[1]/button')
# button3.click()
# WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="simplifiedSiteContainer"]/div/div/div[3]/div[25]/div[2]/div/div/div/div/div[2]/div')))
# print('Website is loaded')
# time.sleep(4)
# # button4 = browser.find_element(By.XPATH, '//*[@id="admin.navigationBar.diagnostic.TITLE"]')
# # button4.click()
# menu = browser.find_element(By.XPATH, "/html/body/main-view/div/div[1]/app-header/main-menu/nav-item[6]/div/nav-menu-link/span/span")
# hidden_submenu = browser.find_element(By.XPATH, "/html/body/main-view/div/div[1]/app-header/main-menu/nav-item[6]/div/ng-transclude/div/div[12]/nav-link/a")
#
# button5 = browser.find_element(By.XPATH, "/html/body/main-view/div/div[1]/app-header/main-menu/nav-item[6]/div/ng-transclude/div/div[12]/nav-link/a/span")
# print("Direction found")
# time.sleep(3)
# browser.implicitly_wait(5)
# ActionChains(browser).move_to_element(button5).click(button5).perform()
# time.sleep(3)

"""
Pobieranie pliku i sprawdzanie czy sie zebrał
# import time
# import os
# 
# def download_wait(path_to_downloads):
#     seconds = 0
#     dl_wait = True
#     while dl_wait and seconds < 20:
#         time.sleep(1)
#         dl_wait = False
#         for fname in os.listdir(path_to_downloads):
#             if fname.endswith('.crdownload'):
#                 dl_wait = True
#         seconds += 1
#     return seconds

https://stackoverflow.com/questions/21746750/check-and-wait-until-a-file-exists-to-read-it
https://stackoverflow.com/questions/4708511/how-to-watch-a-directory-for-changes
https://stackoverflow.com/questions/597903/monitoring-contents-of-files-directories
"""
"""
import os.path
import base64
import json
import re
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import logging
import requests

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.modify']

def readEmails():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(               
                # your creds file here. Please create json file as here https://cloud.google.com/docs/authentication/getting-started
                'my_cred_file.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
        messages = results.get('messages',[]);
        if not messages:
            print('No new messages.')
        else:
            message_count = 0
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()                
                email_data = msg['payload']['headers']
                for values in email_data:
                    name = values['name']
                    if name == 'From':
                        from_name= values['value']                
                        for part in msg['payload']['parts']:
                            try:
                                data = part['body']["data"]
                                byte_code = base64.urlsafe_b64decode(data)

                                text = byte_code.decode("utf-8")
                                print ("This is the message: "+ str(text))

                                # mark the message as read (optional)
                                msg  = service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}).execute()                                                       
                            except BaseException as error:
                                pass                            
    except Exception as error:
        print(f'An error occurred: {error}')
"""