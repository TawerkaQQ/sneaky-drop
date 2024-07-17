import os
import zipfile

from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

def get_chrome_driver(use_proxy: bool = False, use_user_agent: bool = False,
                      proxy_host: str = 'PROXY_HOST1', proxy_port: str = 'PROXY_PORT1',
                      proxy_user: str = 'PROXY_USER1', proxy_pass: str = 'PROXY_PASS'):
    chrome_options = webdriver.ChromeOptions()

    if use_proxy:
        print('using proxy')
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

        plugin_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        plugin_file = 'proxy_auth_plugin.zip'
        with zipfile.ZipFile(os.path.join(plugin_path, plugin_file), 'w') as zp:
            zp.writestr('manifest.json', manifest_json)
            zp.writestr('background.js', background_js)
        chrome_options.add_extension(os.path.join(plugin_path, plugin_file))

    if use_user_agent:
        pass

    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=chrome_options)
    return driver