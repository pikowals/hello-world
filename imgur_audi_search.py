from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import bs4
import os
import requests

s = Service(r'C:\Users\pkowalski7\Downloads\chromedriver_win32\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://imgur.com/')
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[3]/span').click()
browser.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div[4]/div/form/input').send_keys('audi')
action = ActionChains(browser)
action.send_keys(Keys.ENTER)
action.perform()
os.makedirs('imgur_audi', exist_ok=True)

current_URL = browser.current_url
res = requests.get(current_URL)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,features="html.parser")
audiElem = soup.select('a[class="image-list-link"]')
for i in range(len(audiElem)):
    AudiLinks = 'https://imgur.com' + audiElem[i].get('href')
    browser.get(AudiLinks)
    print(AudiLinks)
    soup = bs4.BeautifulSoup(browser.page_source, features="html.parser")
    AudiCont = soup.select('.PostVideo-video-wrapper')
    if AudiCont == []:
        AudiCont = soup.select('.image-placeholder')
    audi_link = AudiCont[0].get('src')
    if audi_link == None:
        Audi_video = AudiCont[0].select('source[type="video/mp4"]')
        audi_link = Audi_video[0].get('src')
    res = requests.get(audi_link)
    print(audi_link)
    if audi_link.endswith('.mp4') or audi_link.endswith('.gif'):
        downloadedFile = open(os.path.join('imgur_audi', os.path.basename(audi_link)),'wb')
    else:
        downloadedFile = open(os.path.join('imgur_audi', f'audi_{i}.jpeg'),'wb')
    print('Downloading file %s ' % audi_link)
    for chunk in res.iter_content(100000):
        downloadedFile.write(chunk)
    downloadedFile.close()


