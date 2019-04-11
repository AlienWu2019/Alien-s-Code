# -*- coding: utf-8 -*-
import scrapy
from myfirstpjt.items import MyfirstpjtItem

class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['sina.com.cn']
    start_urls = (
        'http://slide.news.sina.com.cn/s/slide_1_2841_103185.html#p=1',
        'http://slide.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
    )
    # #定义新的属性url2
    # urls2=("http://www.jd.com",
    #     "http://sina.com.cn",
    #     "http://yum.iqianyue.com",
    # )
    # #重写了start_requests()方法
    # def start_requests(self):
    #     #在该方法中将起始网址设置为从新属性url2中读取
    #     for url in self.urls2:
    #         #调用默认make_requests_from_url()方法生成具体请求，并通过yield返回
    #         yield self.make_requests_from_url(url)

    #重写初始化方法__init__(),并设置参数myurl
    def __init__(self,myurl=None,*args,**kwargs):
        super(WeisuenSpider,self).__init__(*args,**kwargs)
        #通过split()将传递进来的参数以“|”为切割符进行分割，分隔后生成一个列表并赋值给myurllist变量
        myurllist = myurl.split("|")
        for i in myurllist:
            #输出要爬的网址，对应值为接收到的参数
            print("要爬取的网址为：%s"%i)
        #将起始地址设置为传进来的参数中各网址组成的列表
        self.start_urls = myurllist


    def parse(self, response):
        item = MyfirstpjtItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print("以下将显示爬取的网址的标题")
        print(item["urlname"])

