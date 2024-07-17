import os

from dotenv import load_dotenv

load_dotenv()

proxies = [
    {
        'proxy_host': os.getenv('PROXY_HOST1'),
        'proxy_port': os.getenv('PROXY_PORT1'),
        'proxy_user': os.getenv('PROXY_USER1'),
        'proxy_pass': os.getenv('PROXY_PASS1'),
    },
]


def get_proxy_group(index):
    proxy_host = proxies[index]['proxy_host']
    proxy_port = proxies[index]['proxy_port']
    proxy_user = proxies[index]['proxy_user']
    proxy_pass = proxies[index]['proxy_pass']
    return proxy_host, proxy_port, proxy_user, proxy_pass
