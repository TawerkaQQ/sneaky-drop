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
from faker import Faker

# from pass_generator import generator as gen
from driver import get_chrome_driver
from config.url_config import GOOGLE_MAIL_REGISTER_URL

class Ozon_reg():
    def __init__(self):
        self.driver = get_chrome_driver(use_proxy=True, use_user_agent=False)
        self.url = 'https://www.ozon.ru/'

    def ozon_reg(self):

        try:
            wait = WebDriverWait(self.driver, 10)
            self.driver.get(self.url)
            time.sleep(7)
            #
            come_in = self.driver.find_element(By.CLASS_NAME, "d409-a")
            time.sleep(2)
            come_in.click()
            time.sleep(4)

            tel_input = self.driver.find_element(By.NAME, "autocomplete")
            tel_input.send_keys('987')
            time.sleep(1000)

        except:
            come_in = self.driver.find_element(By.CLASS_NAME, "b6012-a3")
            time.sleep(2)
            come_in.click()
            time.sleep(1000)
            pass


if __name__ == '__main__':

    sel_ozon = Ozon_reg()
    sel_ozon.ozon_reg()