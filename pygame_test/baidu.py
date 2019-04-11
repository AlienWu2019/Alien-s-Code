import requests
from pyquery import PyQuery as pq
import pymysql
import re

class Baike_baidu:
    def __init__(self,key):
        url1="https://baike.baidu.com/item/"
        self.url = url1+key

    #获取网页的html
    def html(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
        req=requests.get(self.url,headers=headers)
        html=req.content
        html_doc=str(html,'utf-8')
        return html_doc

    #抓取百度百科概述
    def search_news_Summary(self):
        content=pq(self.html())
        result=content(".lemma-summary .para").text()
        result2 = result.replace('\xa0','')
        result3 = result2.replace(' ', '')
        return result3

    #抓取表格字条
    def search_news_form(self):
        content=pq(self.html())
        result1=content('.basic-info')
        result2=result1('.basicInfo-block').text()
        result3 = result2.replace('\n',':')
        result4 = result3.replace('\xa0','')
        return result4

    #抓取标题名称
    def search_news_title(self):
        search_news_str='<h2 class="title-text"><span class="title-prefix">.*?</span>(.*?)</h2>'
        content = pq(self.html())
        title1 = content('.para-title')
        title2 = title1('.title-text')
        str_title2 = str(title2)
        search = re.compile(search_news_str)
        result = search.findall(str_title2)
        return result

    #抓取内容:
    def search_news_content(self):
        search_news_str = '<div class="para" label-module="para">(.*)</div>'
        search_news_str1 = '<[^>]*>'
        content = pq(self.html())
        search = re.compile(search_news_str)
        str_content = str(content)
        result = search.findall(str_content)
        result_clear = result.remove(result[0])
        result_str = "".join(result)
        search2 = re.compile(search_news_str1)
        result_str2 = search2.sub('',result_str)
        return result_str2

key=input("请输入要搜索的内容：")
a=Baike_baidu(key)
print("总体概述:")
print(a.search_news_Summary())
print("----------------------")
print("表格内容:")
print(a.search_news_form())
print("-----------------------")
print("主要内容:")
print(a.search_news_content())


boolean = input("是否将数据存进数据库?(y/n):")
if boolean == "y":
    db = pymysql.connect("localhost", "root", "root", "search_news", charset='utf8')
    cur = db.cursor()
    sql = "insert into baidu_baike (title,form,content) values('{0}','{1}','{2}')".format(a.search_news_Summary(),a.search_news_form(),a.search_news_content())
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
else:
    exit()