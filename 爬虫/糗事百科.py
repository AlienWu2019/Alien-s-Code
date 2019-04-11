import requests
from pyquery import PyQuery as pq

url="https://www.qiushibaike.com/text/"
req=requests.get(url)
html=req.text
assert req.status_code==200
html_doc=pq(html)
contents=html_doc("div .col1")
for menbers in contents:
    i=pq(menbers)
    menbers_list=i("div")
    for item in menbers_list:
        j=pq(i)
        content=j("div .content").text()
        print(content)
