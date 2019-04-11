import scrapy
from bs4 import BeautifulSoup
from ..items import AppledailyItem
import re
import requests


class appledaily(scrapy.Spider):
    name = 'appledaily'
    #重写start_url
    def start_requests(self):
        print("网速较慢，耐心等待!")
        for i in range(1,4):
            self.url = 'https://tw.video.appledaily.com/actionnews/ajaxmore/appledaily/entertainment/20190317/1532811/{}'.format(i)
            #print(self.url)
            yield scrapy.Request(url=self.url,callback=self.parse)

    def parse(self, response):
        """该函数主要是处理主页面内容，包括获得新闻的日期，标题和链接，并且把链接回调给parse_deal进行下一步处理获得人气和视频链接"""
        html = BeautifulSoup(response.body)
        str_html = str(html) #转成字符串进行正则匹配截取信息
        apple = AppledailyItem() #初始化itmes中的AppledailyItem把信息存进去
        # 收集新闻日期
        pattern_date = r'<div class="datetime">(.*?)</div>'
        apple['date'] = re.compile(pattern_date).findall(str_html)
        #收集标题
        pattern_title = r'<h2>(.*?)</h2>'
        apple['title'] = re.compile(pattern_title).findall(str_html)
        #收集链接
        pattern_link = r'<a href="(.*?)">'
        links = []
        a=""
        native_link = re.compile(pattern_link).findall(str_html)
        #收集人气
        list_view = []
        list_video = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
        }
        proxies = {'https': 'http://127.0.0.1:1080'}
        for i in native_link:
            a ='https://tw.video.appledaily.com/'+i
            # print(a)
            links.append(a)
            # yield scrapy.Request(url=a, callback=self.parse_deal)
            text = requests.get(a,headers=headers,proxies=proxies).text
            text_str = str(text)
            # 收集人气
            pattern_view = r'<span class="vver" style="width:105px;margin-right:13px;overflow:hidden;" >(.*?)</span>'
            view = re.compile(pattern_view).findall(text_str)[0]
            list_view.append(view)
            # 收集视频链接
            pattern_video = "var videoUrl = '(.*?).mp4'"
            video = re.compile(pattern_video).findall(text_str)[0] + '.mp4'
            list_video.append(video)
        apple['links'] = links
        apple['view'] = list_view
        apple['video_link'] = list_video
        # print(apple['date'])
        # print(apple['title'])
        # print(apple['links'])
        # print(apple['view'])
        # print(apple['video_link'])
        return apple

    # def parse_deal(self,response):
    #     """该函数主要是从parse中获得的新闻url进行分析获得人气和视频链接的信息"""
    #     html = BeautifulSoup(response.body)
    #     str_html = str(html)  #转成字符串进行正则匹配截取信息
    #     apple = AppledailyItem()
    #     #收集人气
    #     pattern_view = r'<span class="vver" style="width:105px;margin-right:13px;overflow:hidden;" >(.*?)</span>'
    #     self.view = re.compile(pattern_view).findall(str_html)[0]
    #     #收集视频链接
    #     pattern_video = "var videoUrl = '(.*?).mp4'"
    #     self.video = re.compile(pattern_video).findall(str_html)[0]+'.mp4'
    #     apple['view'] = self.view
    #     apple['video_link'] = self.video
    #     return apple





