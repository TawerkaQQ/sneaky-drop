import os
import zipfile
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from dotenv import load_dotenv
from config.proxy_config import get_proxy_group


def get_chrome_driver(use_proxy: bool = False, use_user_agent: bool = False, proxy_group: int = 0):
    chrome_options = webdriver.ChromeOptions()

    if use_proxy:
        print('using proxy')
        proxy_host, proxy_port, proxy_user, proxy_pass = get_proxy_group(proxy_group)
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (proxy_host, proxy_port, proxy_user, proxy_pass)
        
        plugin_path = os.path.abspath(os.path.join(os.getcwd(), 'config'))
        plugin_file = 'proxy_auth_plugin.zip'
        print(os.path.join(plugin_path, plugin_file))
        with zipfile.ZipFile(os.path.join(plugin_path, plugin_file), 'w') as zp:
            zp.writestr('manifest.json', manifest_json)
            zp.writestr('background.js', background_js)
        chrome_options.add_extension(os.path.join(plugin_path, plugin_file))

    if use_user_agent:
        pass

    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=chrome_options)
    return driver
