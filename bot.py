import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import traceback
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import urllib2
from bs4 import BeautifulSoup
from collections import defaultdict
import json

# load your shit from a json file
config = None
with open('password.json', 'r') as f:
    config = json.load(f)


# seems like pointless method now
def get_shoes():
    url = 'http://store.nike.com/us/en_us/pw/mens-shoes/7puZoi3'
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    soup.prettify()

    mydivs = soup.find_all("div", class_="grid-item fullSize")
    shoes = defaultdict()
    for shoe in mydivs:
        s_name = shoe.find(
            'div', attrs={'class': 'product-name '}).text.strip().replace('\n', ' ')
        shoes[s_name] = shoe.find('a')['href']
    return shoes


def nike_login(driver):
    url = 'http://www.nike.com/us/en_us/'
    driver.get(url)
    element = driver.find_element_by_class_name('exp-join-login')
    while element.is_enabled() is False or element.is_displayed() is False:
        WebDriverWait(driver, 1)

    element.click()
    driver.switch_to_alert()
    email = driver.find_element_by_name('emailAddress')
    while email.is_enabled() is False or email.is_displayed() is False:
        WebDriverWait(driver, 1)
    email.send_keys(config['email'])

    password = driver.find_element_by_name('password')
    while password.is_enabled() is False or password.is_displayed() is False:
        WebDriverWait(driver, 1)
    password.send_keys(config['password'])  # your pass
    driver.find_element_by_class_name("nike-unite-submit-button").click()

    wait = WebDriverWait(driver, 3)
    wait.until(EC.presence_of_element_located((By.ID, 'exp-profile-dropdown')))


def add_to_cart(driver, url, size):
    driver.get(url)
    driver.find_element_by_class_name("nsg-form--drop-down--label").click()
    sizes = driver.find_elements_by_class_name("nsg-form--drop-down--option")
    found = False
    for s in sizes:
        if s.text == size:
            s.click()
            found = True
            break
    if not found:
        raise Exception("Shoe size {} not found!".format(size))

    driver.find_element_by_id('buyingtools-add-to-cart-button').click()
    time.sleep(.5)
def main():
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference(
        'dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    firefox_profile.set_preference("browser.download.folderList", 2)
    firefox_profile.set_preference('browser.migration.version', 9001)
    driver = webdriver.Firefox(firefox_profile=firefox_profile)

    try:
        url = 'http://store.nike.com/us/en_us/pd/lunarcharge-essential-bn-mens-shoe/pid-11652135/pgid-11870795'
        size = "10"

        nike_login(driver)
        time.sleep(.5)

        add_to_cart(driver, url, size)

        # will terminate after this
        raw_input("Shoe in checkout :)\nPress Enter to end ...")

    except Exception as e:
        traceback.print_exc()
    finally:
        driver.close()


if __name__ == '__main__':
    main()
