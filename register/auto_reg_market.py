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
from dotenv import load_dotenv

from pass_generator import generator as gen
from driver import get_chrome_driver

load_dotenv()


class MarketReg:
    google_mail_register_url = os.getenv('GOOGLE_MAIL_REGISTER_URL')
    def __init__(self):
        self.driver = get_chrome_driver(use_proxy=True, use_user_agent=False)
        self.fake = Faker("ru_RU")

    def gmail_reg(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(MarketReg.google_mail_register_url)
        time.sleep(100000)
        elem = self.driver.find_element(By.CLASS_NAME, "Xb9hP")
        elem = (elem.find_element(By.XPATH, "//input[@data-initial-value]"))
        time.sleep(1)
        elem.send_keys('mail@gmail.com')
        time.sleep(1)

        create_acc = self.driver.find_elements(By.TAG_NAME, "button")
        for next in create_acc:
            if next.text == 'Создать аккаунт':
                time.sleep(1)
                next.click()

        time.sleep(1)
        for_me = self.driver.find_element(By.CLASS_NAME, "VfPpkd-StrnGf-rymPhb-b9t22c")
        time.sleep(1)
        for_me.click()

        fio = self.driver.find_elements(By.XPATH, "//input[@data-initial-value]")
        time.sleep(1)
        fio[0].send_keys(self.fake.first_name())
        time.sleep(1)
        fio[1].send_keys(self.fake.last_name_male())

        next1 = self.driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
        time.sleep(1)
        next1.click()

        day_field = wait.until(EC.visibility_of_element_located((By.ID, "day")))
        day_field.send_keys(random.randint(1, 30))

        year_field = wait.until(EC.visibility_of_element_located((By.ID, "year")))
        year_field.send_keys(random.randint(1980, int(datetime.datetime.today().year)) - 15)

        month = self.driver.find_element(By.CLASS_NAME, "gNnnTd")
        month_select = Select(month)
        options = month_select.options
        random_index = random.randint(1, len(options) - 1)
        month_select.select_by_index(random_index)

        gender = wait.until(EC.visibility_of_element_located((By.ID, "gender")))
        gender_select = Select(gender)
        options = gender_select.options
        random_index = random.randint(1, len(options) - 3)
        gender_select.select_by_index(random_index)

        next2 = self.driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
        time.sleep(1)
        next2.click()

        # КОСТЫЛЬ
        try:
            gmail = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "jOkGjb")))
            gmail.click()

        except:
            print("Reboot script")


        next3 = self.driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
        time.sleep(1)
        next3.click()


        password = gen(15)
        print(password)
        passw = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        time.sleep(1)
        passw.send_keys(password)

        passw1 = wait.until(EC.visibility_of_element_located((By.NAME, "PasswdAgain")))
        time.sleep(1)
        passw1.send_keys(password)

        next4 = self.driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
        time.sleep(1)
        next4.click()

        # time.sleep(100)
        # tel = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "VfPpkd-NSFCdd-Ra9xwd")))
        # time.sleep(1)
        # tel.send_keys('98951251')




        time.sleep(1000)
        self.driver.close()
        return self

    def ozon_reg(self):
        pass

    def wb_reg(self):
        pass

    def yandex_reg(self):
        pass


if __name__ == '__main__':
    market = MarketReg()
    # market.test()
    market.gmail_reg()