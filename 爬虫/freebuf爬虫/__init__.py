import requests
headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
def use_proxy(proxy_addr,url):

    proxy = {"https": proxy_addr}
    req = requests.post(url,headers=headers,proxies=proxy)
    return req.text

a=use_proxy("http://127.0.0.1:1080","https://www.freebuf.com/vuls/195656.html")
print(a)