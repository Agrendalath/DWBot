#!/usr/bin/env python
import credentials
import os
import time
from pyvirtualdisplay import Display
from retrying import retry
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple


@retry(wait_fixed=6000, stop_max_attempt_number=3)
def find_login_fields(driver: Firefox) -> Tuple[WebElement, WebElement]:
    """Bypass CloudFlare DDoS protection."""
    return driver.find_element_by_name('usrname'), \
        driver.find_element_by_name('passwrd')


payload = {
        'usrname': os.environ.get('login', credentials.login),
        'passwrd': os.environ.get('password', credentials.password),
        'autologin': 'on',
        'login': 'Zaloguj'
}
login_url = 'https://darkwarez.pl/forum/login.php'
url = "https://www.darkwarez.pl/forum"

display = Display(visible=0, size=(800, 600))
display.start()

ffprofile = FirefoxProfile()
ffprofile.add_extension(extension='adblock.xpi')
driver = Firefox(firefox_profile=ffprofile)

driver.get(login_url)

username, password = find_login_fields(driver)

username.send_keys(payload['usrname'])
password.send_keys(payload['passwrd'])

driver.find_element_by_name('login').click()

time.sleep(10)  # Wait for page to load

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

display.stop()
