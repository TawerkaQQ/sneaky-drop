from selenium import webdriver

def get_chrome_driver(use_proxy: bool = False, use_user_agent: bool = False):
    chrome_options = webdriver.ChromeOptions()

    if use_proxy:
        pass

    if use_user_agent:
        pass

    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=chrome_options)
    return driver