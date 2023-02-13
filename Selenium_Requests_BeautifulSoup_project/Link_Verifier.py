from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import bs4
s = Service(r'C:\Users\pkowalski7\Downloads\chromedriver_win32\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://automatetheboringstuff.com/2e/chapter12/')
res = requests.get(browser.current_url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features="html.parser")
hrefLinks = soup.select('a')
tabNotWorking = []
tabWorking = []
for i in hrefLinks:
    linkToBeChecked = i.get('href')
    try:
        checker = requests.get(linkToBeChecked)
        if checker == 'Response [404]':
            raise Exception
        tabWorking.append(linkToBeChecked)
        print('Działajacy link %s '% linkToBeChecked)
    except Exception:
        tabNotWorking.append(linkToBeChecked)
        print('Mamy exception na linku %s  ' % (linkToBeChecked))


print('Działajace linki\n %s ' %tabWorking)
print('Niedziałajace linki\n %s ' %tabNotWorking)

