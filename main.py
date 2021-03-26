import time
from selenium import webdriver
import winsound

browser = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')

browser.get('https://www.alternate.de/Grafikkarten/AMD-Grafikkarten')
browser.maximize_window()
freq = 2500
dur = 1000
buyButton = False
while not buyButton:
    try:
        link = browser.find_element_by_link_text("RX 6700 XT").click()
        winsound.Beep(freq, dur)
        print("Knopf gedrückt")
        buyButton = True
    except:
        print("Button nicht bereit")
        time.sleep(1)
        browser.refresh()
