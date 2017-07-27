#!/usr/bin/env python
import credentials
import os
import requests
import time
from pyvirtualdisplay import Display
from selenium import webdriver

payload = {
        'usrname': os.environ.get('login', credentials.login),
        'passwrd': os.environ.get('password', credentials.password),
        'autologin': 'on',
        'login': 'Zaloguj'
}
login_url = 'https://darkwarez.pl/forum/login.php'
url = "https://www.darkwarez.pl/forum"

s = requests.Session()

display = Display(visible=0, size=(800, 600))
display.start()

ffprofile = webdriver.FirefoxProfile()
ffprofile.add_extension(extension='adblock.xpi')
driver = webdriver.Firefox(firefox_profile=ffprofile)

driver.get(login_url)
username = driver.find_element_by_name('usrname')
password = driver.find_element_by_name('passwrd')

username.send_keys(payload['usrname'])
password.send_keys(payload['passwrd'])

driver.find_element_by_name('login').click()

time.sleep(10)

# driver.get_screenshot_as_file('test.png')

aElements = driver.find_elements_by_tag_name("a")
for name in aElements:
    if (name.get_attribute("href") is not None
            and "javascript:void" in name.get_attribute("href")):
        if name.is_displayed():
            name.click()
            print("Done.")
        else:
            print("You've already collected diamonds today.")
        break

# driver.get_screenshot_as_file('test2000.png')

display.stop()
