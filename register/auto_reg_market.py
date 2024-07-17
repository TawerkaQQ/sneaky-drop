import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from driver import get_chrome_driver

class Market_reg:
    def __init__(self):
        self.driver = get_chrome_driver(use_proxy=True, use_user_agent=True)


    def gmail_reg(self, mail: str, first_name: str, second_name: str):

        '''
        Дописать более адекватный таймслип и закончить регу
        '''
        self.driver.get("https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmail.google.com%2Fmail&ec=GAlAFw&hl=ru&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S1493690269%3A1721053389183545&ddm=0")

        elem = self.driver.find_element(By.CLASS_NAME, "Xb9hP")
        elem = (elem.find_element(By.XPATH, "//input[@data-initial-value]"))
        time.sleep(3)
        elem.send_keys(mail)
        time.sleep(3)

        create_acc = self.driver.find_elements(By.TAG_NAME, "button")
        for next in create_acc:
            if next.text == 'Создать аккаунт':
                time.sleep(3)
                next.click()

        time.sleep(3)
        for_me = self.driver.find_element(By.CLASS_NAME, "VfPpkd-StrnGf-rymPhb-b9t22c")
        time.sleep(3)
        for_me.click()

        fio = self.driver.find_elements(By.XPATH, "//input[@data-initial-value]")
        time.sleep(3)
        fio[0].send_keys(first_name)
        time.sleep(3)
        fio[1].send_keys(second_name)

        next1 = self.driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
        time.sleep(3)
        next1.click()

        time.sleep(1000)
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
    market.gmail_reg('mail@gmail.com', 'Ivan', 'Ivanov')
