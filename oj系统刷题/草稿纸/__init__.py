import requests
from bs4 import BeautifulSoup as bs
import re
from bs4 import BeautifulSoup as bs

proxies = {'https':'http://127.0.0.1:1080'}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
url = "https://tw.video.appledaily.com/actionnews/ajaxmenu/appledaily/hot/20190317/1532811/14"
html = bs(requests.get(url,headers=headers,proxies=proxies).content,'lxml')
print(html)
# req = str(requests.get(url,headers=headers,proxies=proxies).text)
# pattern = '<span>(.*?)</span>'
# pattern_title = '<h4>(.*?)</h4>'
# pattenr_link = '<a href="(.*?)">'
# pattern_view = '<span class="vver" style="width:105px;margin-right:13px;overflow:hidden;" >(.*?)</span>'
# pattern_video = "var videoUrl = '(.*?).mp4'"
# print(re.compile(pattern_view).findall(req)[0])
# date = re.compile(pattern).findall(str(html))
# print(date)
# title = re.compile(pattern_title).findall(str(html))
# print(title)
# link = re.compile(pattenr_link).findall(req)
# links=[]
# a = ""
# for i in link:
#     a+='https://tw.video.appledaily.com/'+i
#     links.append(a)
# url=[i for i in links]
# print(url)
# start_url = ['https://tw.video.appledaily.com/actionnews/ajaxmenu/appledaily/hot/20190317/1532811/{}'.format(i) for i in range(1,14)]
# print(start_url)