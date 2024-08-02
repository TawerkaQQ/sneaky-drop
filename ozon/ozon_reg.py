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
from config.url_config import GOOGLE_MAIL_REGISTER_URL, OZON_URL

class OzonReg():
    def __init__(self):
        self.driver = get_chrome_driver(use_proxy=True, use_user_agent=True)
        self.wait = WebDriverWait(self.driver, 20)

    def ozon_reg(self):
        self.driver.get(OZON_URL)
        self.driver.maximize_window()
        time.sleep(4)
        reload_page = self.driver.find_element(By.XPATH, "//button[@class='rb']")
        time.sleep(1)
        reload_page.click()
        time.sleep(15)
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
            time.sleep(20)
            element.send_keys('999 694 46 82')
            time.sleep(4)
            # self.driver.switch_to.frame(iframe)

            sign_in = self.driver.execute_script(
                """
                            var inputElement = document.evaluate("//button[@type='submit']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                            return inputElement.singleNodeValue;
                                    """
                )
            sign_in.click()
            time.sleep(4)

            i_agree = self.driver.execute_script(
                """
                            var inputElement = document.evaluate("//input[@type='checkbox']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                            return inputElement.singleNodeValue;
                                    """
            )
            time.sleep(4)
            i_agree.click()

            # get_new_code = self.driver.execute_script(
            #     """
            #                 var inputElement = document.evaluate("//div[@class='c806-a']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
            #                 return inputElement.singleNodeValue;
            #                         """
            # )
            # time.sleep(120)
            # get_new_code.click()
            time.sleep(4000)


if __name__ == '__main__':

    sel_ozon = OzonReg()
    sel_ozon.ozon_reg()
