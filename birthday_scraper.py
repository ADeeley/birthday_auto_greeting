#-----------------------------
# Version- 0.1 
# By Adam Deeley
#-----------------------------

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_html():
    URL = "https://www.facebook.com/events/birthdays"
    HTML = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(HTML.decode('utf-8'), 'html.parser')

    #titles = soup.findAll('h2')
    return soup

def loginFB():
    '''
    Logs into Facebook homepage with the logins provided. 
  
    -  opt = provides webdriver with userdata to sign in to chrome as a user and not
    start a new session.

    -  browser = a variable to start up the webdriver using Chrome with the opt
    settings. Gets the webpage.
    '''
    opt = webdriver.ChromeOptions()
    opt.add_argument("user-data-dir=C:\\Users\\Adam\\AppData\\Local\\Google\\Chrome\\User Data")
    
    browser = webdriver.Chrome(chrome_options=opt)
    browser.get('https://en-gb.facebook.com/login/')
    
    emailElem = browser.find_element_by_id('email')
    emailElem.send_keys('07934884157')
    
    passElem = browser.find_element_by_id('pass')
    passElem.send_keys('TangoDjango73?')
    passElem.submit()
    
    browser.get("https://www.facebook.com/events/upcoming?ref=46&amp;action_history=null")
