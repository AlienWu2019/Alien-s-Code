import requests
import re

proxies = {"https": "http://127.0.0.1:1080"}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
url="https://www.google.com.hk/"
req = requests.get(url,headers=headers,proxies=proxies)
html=req.text
print(html)

