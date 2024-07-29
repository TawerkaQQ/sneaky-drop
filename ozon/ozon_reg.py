import datetime
import time
import random
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
from bs4 import BeautifulSoup

# from pass_generator import generator as gen
from driver import get_chrome_driver
from config.url_config import GOOGLE_MAIL_REGISTER_URL

class Ozon_reg():
    def __init__(self):
        self.driver = get_chrome_driver(use_proxy=True, use_user_agent=False)
        self.url = 'https://www.ozon.ru/'
        self.wait = WebDriverWait(self.driver, 20)

    def ozon_reg(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(4)
        come_in = self.find_come_in_element()

    def find_come_in_element(self):
        element = self.driver.execute_script("""
            var spanElements = document.evaluate("//span[contains(text(), 'Войти')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
            return spanElements.singleNodeValue;
        """)
        if not element:
            print('no')
            time.sleep(400)
        else:
            time.sleep(1)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            time.sleep(3)
            element.click()
            time.sleep(2)
            iframe = self.driver.execute_script("""
                var inputElement = document.evaluate("//iframe[@id='authFrame']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                return inputElement.singleNodeValue;
            """)
            self.driver.switch_to.frame(iframe)
            element = self.driver.execute_script("""
                            var inputElement = document.evaluate("//input", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                            return inputElement.singleNodeValue;
                        """)
            time.sleep(10)
            element.send_keys('11111')
            time.sleep(10000)

    def find_come_in_element_bs4(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        res = soup.find('svg', {'width': '24', 'height': '24'})
        print(len(res))

    def connect_to_ozon(self):
        self.driver.get(self.url)
        time.sleep(3)
        return self


if __name__ == '__main__':

    sel_ozon = Ozon_reg()
    sel_ozon.ozon_reg()