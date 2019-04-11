# -*- coding: UTF-8 -*-
import requests
from pyquery import PyQuery as pq

url = "http://www.baidu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}
req = requests.get(url,headers=headers)
html = req.text
html_doc = pq(html)
print(html_doc)