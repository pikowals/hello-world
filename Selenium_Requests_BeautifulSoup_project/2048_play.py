from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


s = Service(r'C:\Users\pkowalski7\Downloads\chromedriver_win32\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://play2048.co/')
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/p/span/button[2]').click()
for i in range(20):
    actions = ActionChains(browser)
    actions.send_keys(Keys.UP)
    actions.perform()
    sleep(1)
    actions = ActionChains(browser)
    actions.send_keys(Keys.LEFT)
    actions.perform()
    sleep(1)
    actions = ActionChains(browser)
    actions.send_keys(Keys.RIGHT)
    actions.perform()
    sleep(1)
    actions = ActionChains(browser)
    actions.send_keys(Keys.DOWN)
    actions.perform()
    sleep(1)
