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

from .driver import get_chrome_driver
from config.url_config import GOOGLE_MAIL_REGISTER_URL, OZON_URL

class OzonReg():
    def __init__(self):
        self.driver = get_chrome_driver(use_proxy=True, use_user_agent=False)
        self.wait = WebDriverWait(self.driver, 20)

    def ozon_reg(self):
        self.driver.get(OZON_URL)
        self.driver.maximize_window()
        time.sleep(4)
        self.find_come_in_element()

    def find_come_in_element(self):
        element = self.driver.execute_script("""
            var spanElements = document.evaluate("//span[contains(text(), 'Войти')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
            return spanElements.singleNodeValue;
        """)
        if not element:
            print('no')
            time.sleep(400)
        else:
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
            time.sleep(5)
            element.send_keys('11111')
            time.sleep(10000)
