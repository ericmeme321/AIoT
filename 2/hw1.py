from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import shutil
import os

browser = webdriver.Chrome('C:/AIoT/2/chromedriver.exe')
browser.get('https://aiot.kaitechstudio.com/Homework/')

browser.find_element_by_name('userID').send_keys('ttu410606224')
time.sleep(1)
browser.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(1)

for i in range(0,200):
    q1 = browser.find_element_by_name('Q1')
    q1 = q1.get_attribute('value')
    a1 = q1.replace('|','ttu410606224')
    a1 = a1.replace(' ','')
    browser.find_element_by_name('Q1a').send_keys(a1)

    q2 = browser.find_element_by_name('Q2')
    q2 = q2.get_attribute('value')

    num1 = ''
    num2 = ''
    flg = 1
    for item in q2:
        if item == '=':
            break
        if item == ' ':
            flg += 1
        elif flg == 1:
            num1 += item
        elif flg == 2:
            ope = item
        elif flg == 3:
            num2 += item

    num1 = int(num1)
    num2 = int(num2)
    a2 = 0

    if ope == '+':
        a2 = num1 + num2
    elif ope == '-':
        a2 = num1 - num2
    elif ope == '*':
        a2 = num1 * num2
    elif ope == '/':
        a2 = num1 / num2
    elif ope == '%':
        a2 = num1 % num2

    browser.find_element_by_name('Q2a').send_keys(a2)
    browser.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(2)