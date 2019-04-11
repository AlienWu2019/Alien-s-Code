#此脚本包括创建文件夹，利用多线程爬取
import requests
import os
import time
import threading
from bs4 import BeautifulSoup

def download_page(url):
    """
     用于下载页面
    """
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3137.400"}
    r = requests.get(url,headers=headers)
    return r.text

def get_pic_list(html):
    """
    获取每个页面得套图列表，之后循环调用get——pic函数获取图片
    """
    #bs4得html解析器
    soup = BeautifulSoup(html,'html.parser')
    pic_list = soup.find_all('ul',class_='mod-pic--video')
    for i in pic_list:
        a_tag = i.find('li').find('img')
        link = a_tag.get('src')
        text = a_tag.get_text()
        return link,text

