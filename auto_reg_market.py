import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Market_reg:
    def __init__(self):
        self.driver = webdriver.Chrome()


    def gmail_reg(self, mail: str):

        '''
        Дописать более адекватный таймслип и закончить регу
        '''
        self.driver.get("https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmail.google.com%2Fmail&ec=GAlAFw&hl=ru&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S1493690269%3A1721053389183545&ddm=0")

        #paste mail
        elem = self.driver.find_element(By.CLASS_NAME, "Xb9hP")
        elem = elem.find_element(By.XPATH, "//input[@data-initial-value]").send_keys(mail)
        time.sleep(100)
        self.driver.close()

        return None

    def ozon_reg(self):
        pass

    def wb_reg(self):
        pass

    def yandex_reg(self):
        pass

    pass


if __name__ == '__main__':
    market = Market_reg()
    # market.test()
    market.gmail_reg('mail@bk.ru')
