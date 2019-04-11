import requests
import re
from pyquery import PyQuery as pq

class travelNews:
    #url处理
    def __init__(self,lname):
        url =  "http://www.mafengwo.cn/search/s.php?q={0}&seid=B79E7F0E-51EA-4C73-B669-E786E4FC59DC".format(lname)
        self.url = url
    #获取城市总体攻略html
    def getUrl(self):
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400'
        }
        req = requests.get(self.url,headers=headers)
        html = req.text
        return html
    #筛选出城市总体的攻略信息
    def searchStrategy_total(self):
        pattern = ' <div class="ser-nums">[^·]* <div class="_j_search_section" data-category="hotel">'
        search = re.compile(pattern)
        news = search.findall(self.getUrl())
        return news[0]
    #过滤并收集信息
    def collect_total(self):
        pattern = '<a href=".*?" target="_blank" class="_j_search_link">.*?</a>'
        search = re.compile(pattern)
        collection = search.findall(self.searchStrategy_total())
        return collection
    #筛选出城市酒店攻略信息
    def searchStrategy_hotel(self):
        pattern = '<div class="_j_search_section" data-category="hotel">[^·]* <div class="_j_search_section" data-category="article_gonglve">'
        search = re.compile(pattern)
        news = search.findall(self.getUrl())
        return news[0]
    #过滤并收集信息
    def collect_hotel(self):
        pattern = '<a href=".*?" target="_blank" class="_j_search_link">.*?</a>'
        search = re.compile(pattern)
        collection = search.findall(self.searchStrategy_hotel())
        return collection


lname = input()
a = travelNews(lname)
news_total = a.collect_total()
news_hotel = a.collect_hotel()
print("总体攻略为:")
for i in news_total:
    print(i)
print()
print("酒店攻略为:")
for i in news_hotel:
    print(i)




