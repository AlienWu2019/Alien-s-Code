import chardet
import requests
html=requests.get('http://jianshu.com')
print(chardet.detect(html.content))