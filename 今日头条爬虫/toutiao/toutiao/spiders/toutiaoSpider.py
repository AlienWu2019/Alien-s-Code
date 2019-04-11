import scrapy
import sqlite3
from bs4 import BeautifulSoup
import re
from ..items import ToutiaoItem
import time


class toutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    domain = ['www.toutiao.com']


    def url_get(self):
        self.conn = sqlite3.connect('toutiao.sqlite')
        cur = self.conn.cursor()
        select_link = cur.execute('select * from toutiao_caijing')
        link_list = []
        for link in select_link:
            link_list.append(link[1])
        return link_list

    def start_requests(self):
        for i in self.url_get():
            yield scrapy.Request(url=i,callback=self.parse)
        self.conn.close()

    def parse(self, response):
        res = BeautifulSoup(response.body,'lxml') #把response结果封装到BeautifulSoup中
        res_str = str(res) #将封装后的结果转为字符串形式以进行匹配中文字处理
        title_html = str(res.select('title')[0])
        pattern_title = r'<title>(.*?)</title>'
        title = re.compile(pattern_title).findall(title_html)[0] #获得网页标题
        content = ','.join(re.findall(r"[a-z,\u4e00-\u9fa5-\d]+",res_str)[4:]) #获得网页汉字内容
        # tag_p = res.find_all('p')[0].text #获得<p>的内容
        # num_chinese_content = re.findall(r"[\u4e00-\u9fa5-\d]+",tag_p) #匹配到中文和数字的内容
        # # list_content = [] #设置一个列表来装提取内容
        # # for i in num_chinese_content:
        # #     try:
        # #         int_num = int(i)
        # #     except:
        # #         list_content.append(i)  # 如果不是数字则提取
        # str_content = ','.join(num_chinese_content)  #提取的content内容
        #print(str_content)
        toutiaoItem = ToutiaoItem()
        toutiaoItem['Date'] = time.ctime()
        toutiaoItem['title'] = title
        toutiaoItem['content'] = content
        return toutiaoItem







