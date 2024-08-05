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
        # reload_page = self.driver.find_element(By.XPATH, "//button[@class='rb']")
        # time.sleep(1)
        # reload_page.click()
        self.driver.refresh()
        time.sleep(15)
        come_in = self.find_come_in_element()

    def find_come_in_element(self):
        element = self.driver.execute_script(JSParser.search_element_script(tag='span', contain_text='Войти'))
        if not element:
            print('no')
            time.sleep(400)
        else:
            time.sleep(3)
            element.click()
            time.sleep(2)
            iframe = self.driver.execute_script(JSParser.search_element_script(tag='iframe', id='authFrame'))
            self.driver.switch_to.frame(iframe)
            element = self.driver.execute_script(JSParser.search_element_script('input'))
            time.sleep(20)
            element.send_keys('999 694 46 82')
            time.sleep(4)
            # self.driver.switch_to.frame(iframe)
            sign_in = self.driver.execute_script(JSParser.search_element_script(tag='button', add_params=True, type='submit') )
            # sign_in = self.driver.execute_script("""
            #                 var inputElement = document.evaluate("//button[@type='submit']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
            #                 return inputElement.singleNodeValue;
            #     """
            #     )
            sign_in.click()
            time.sleep(4)

            i_agree = self.driver.execute_script(JSParser.search_element_script(tag='input', add_params=True, type='checkbox') )
            # i_agree = self.driver.execute_script(
            #     """
            #                 var inputElement = document.evaluate("//input[@type='checkbox']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
            #                 return inputElement.singleNodeValue;
            #                         """
            # )
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

class JSParser:
    @classmethod
    def search_element_script(cls, tag, contain_text=None, add_params=None, **params):
        if not contain_text:
            if not add_params:
                js_script = f"""
                            var element = document.evaluate("//{tag}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                            return element.singleNodeValue;
                """
            else:
                print('yes')
                tags_list = [f'@{x}' for x in params.keys()]
                names_list = [f"'{x}'" for x in params.values()]
                params_list = []
                for x, y in zip(tags_list, names_list):
                    params_list.append(f'{x}=')
                    params_list.append(f'{y}, ')
                params_string = ''.join(params_list)[:-2]
                js_script = f"""
                            var element = document.evaluate("//{tag}[{params_string}]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                            return element.singleNodeValue;
                """
        else:
            js_script = f"""
                        var element = document.evaluate("//{tag}[contains(text(), '{contain_text}')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                        return element.singleNodeValue;
            """
        return js_script

if __name__ == '__main__':

    sel_ozon = OzonReg()
    sel_ozon.ozon_reg()
