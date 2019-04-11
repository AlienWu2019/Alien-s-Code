import requests

def connect_google():
    url="https://www.google.com.hk/"
    headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
            }
    proxies = {"https": "http://127.0.0.1:1080"}
    try:
        req=requests.get(url,headers=headers,proxies=proxies,timeout=3)
        if req.status_code==200:
            return True
    except requests.exceptions.ProxyError  or requests.exceptions.SSLError or requests.exceptions.HTTPError or requests.exceptions.ChunkedEncodingError or requests.exceptions.ConnectionError or requests.exceptions.ContentDecodingError or requests.exceptions.RetryError or requests.exceptions.StreamConsumedError or requests.exceptions.UnrewindableBodyError:
        return False

connect_google()


