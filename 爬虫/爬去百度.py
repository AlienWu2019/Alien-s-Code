import requests
import re

url="https://www.baidu.com/"
req=requests.get(url)
req.encoding='utf-8'
text=req.text
urls = re.findall('<a href=(.*?)>',text,re.S)
for each in urls:
    print(each)
print(re.search('<title>(.*?)</title>',text,re.S).group(1))

url2="https://tieba.baidu.com/f?kw=qq三国&ie=utf-8&pn=0"
for i in range(0,1000,50):
    print(re.sub('pn=\d','pn=%d'%i,url2))
