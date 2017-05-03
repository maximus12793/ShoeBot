from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
import traceback
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import urllib2
from bs4 import BeautifulSoup
from collections import defaultdict
from pdb import set_trace as st
import threading

# driver = webdriver.PhantomJS(
# '/Users/maximilian.roquemore/Desktop/ShoeBot/phantomjs-2.1.1-macosx/bin/phantomjs')


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

    # pprint(shoes)
    # print len(shoes)
    return shoes


# import pdb
# pdb.set_trace()
# grid-item fullSize
'''
Referer = http: // store.nike.com / us / en_us / pd / air - max - 90 - ultra - 2 - essential - mens - shoe / pid - 11242179 / pgid - 11464954
Referer=http://store.nike.com/us/en_us/pd/air - max - 90 - ultra - 2 - essential - mens - shoe / pid - 11242179 / pgid - 11464954
Nike Free RN Flyknit 2017 Men's Running Shoe
pgid-12011507
'''


def nike_login(driver):
    url = 'http://www.nike.com/us/en_us/'
    driver.get(url)
    # element = WebDriverWait(driver, 10).until(
    # lambda x: x.find_element_by_class_name('exp-join-login'))
    # st()
    element = driver.find_element_by_class_name('exp-join-login')
    while element.is_enabled() is False or element.is_displayed() is False:
        WebDriverWait(driver, 1)

    element.click()
    # try:
    # elem = driver.find_element_by_class_name('exp-join-login')
    # WebDriverWait(driver, timeout).until(elem)
    # except:
    # print "SHIT"
    # driver.find_element_by_class_name('exp-join-login').click()
    driver.switch_to_alert()
    email = driver.find_element_by_name('emailAddress')
    while email.is_enabled() is False or email.is_displayed() is False:
        WebDriverWait(driver, 1)
    email.send_keys("")  # your email
    password = driver.find_element_by_name('password')
    while password.is_enabled() is False or password.is_displayed() is False:
        WebDriverWait(driver, 1)
    password.send_keys("")  # your pass
    driver.find_element_by_class_name("nike-unite-submit-button").click()


def add_to_cart(driver, url, size):
    # driver = webdriver.PhantomJS('/Users/maximilian.roquemore/Desktop/ShoeBot/phantomjs-2.1.1-macosx/bin/phantomjs')
    # size = "10"
    # url = 'http://store.nike.com/us/en_us/pd/lunarcharge-essential-bn-mens-shoe/pid-11652135/pgid-11870795'
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
    driver.get('https://secure-store.nike.com/us/checkout/html/cart.jsp?country=US&country=US&l=cart&site=nikestore&returnURL=http://store.nike.com/us/en_us/')


def main():
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image', 2)
    # firefox_profile.set_preference(
    # 'dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    firefox_profile.set_preference("browser.download.folderList", 2)
    firefox_profile.set_preference('browser.migration.version', 9001)

    driver = webdriver.Firefox(firefox_profile=firefox_profile)

    try:
        url = 'http://store.nike.com/us/en_us/pd/lunarcharge-essential-bn-mens-shoe/pid-11652135/pgid-11870795'
        size = "10"

        # 1 thread
        # threading.Thread(target=nike_login).start()
        nike_login(driver)

        # st()

        # find the shoe and start entering info
        # 2 creating the shoe order
        # shoes = get_shoes()
        # url = shoes[shoes.keys()[0]]
        # print "WORKS"

        # 3rd Thread @ the checkout cart
        # threading.Thread(target=add_to_cart, args=[url, size])
        add_to_cart(driver, url, size)

        # get_sizes(url)
        WebDriverWait(driver, 3000)
        st()
    except Exception as e:
        print e, "ERROR"
        traceback.print_exc()
    finally:
        print "Shoe in Checkout :)"
        driver.close()


if __name__ == '__main__':
    main()
