from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import shutil
import os

def getLastestFilename():
    path = 'C:\\Users\\User\\Downloads'
    try:
        filename = max([f for f in os.listdir(path)],\
             key=lambda  x: os.path.getmtime(os.path.join(path, x)))
    except:
        filename = max([f for f in os.listdir(path)],\
             key=lambda  x: os.path.getmtime(os.path.join(path, x)))
    return filename

def changeName(finalName):
    while True:
        filename = getLastestFilename()
        if filename.endswith('.csv'):
            break
    path = 'C:\\Users\\User\\Downloads'
    shutil.move(f'{path}\{filename}', f'{path}\{finalName}')

browser = webdriver.Chrome('./2/chromedriver.exe')
browser.get('https://aiot.kaitechstudio.com/Homework/')

browser.find_element_by_name('userID').send_keys('ttu410606224')
time.sleep(1)
browser.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(1)
item = browser.find_element_by_xpath("//input[@id='q1']")

print(item)