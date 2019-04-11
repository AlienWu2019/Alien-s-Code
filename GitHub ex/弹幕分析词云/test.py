from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib

url1="https://www.discuss.com.hk/forumdisplay.php?fid=46"
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0'}
req = urllib.request.Request(url=url1, headers=headers)
response=urlopen(req)
html=response.read().decode('utf-8','ignore')
print(html)