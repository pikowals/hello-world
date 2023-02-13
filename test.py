from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

while(True):
    s=Service('C:/Users/pikowals/Downloads/chromedriver_win32/chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    url='https://10.44.76.53/'
    browser.get(url)
    button = browser.find_element("id", "details-button")
    button.click()
    button1 = browser.find_element("id", "proceed-link")
    button1.click()
    time.sleep(3)
    log = browser.find_element("id", "login-username")
    log.send_keys("Nemuadmin")
    passw = browser.find_element("id", "login-password")
    passw.send_keys("nemuuser")
    button2 = browser.find_element(By.XPATH, "/html/body/login-root/div/login/div/div/div/div[1]/form/div[3]/p-button/button/span")
    button2.click()
    time.sleep(10)
    pass
