from selenium import webdriver
import time
from bs4 import BeautifulSoup
import threading
import queue
import re
import sqlite3

#定义一个队列用于进行线程间的交流
Queue = queue.Queue()
Queue2 = queue.Queue()
def webopen():
    """该函数主要是处理selenium自动化访问头条然后通过不断刷新获得爬取内容的部分html"""
    #开启chrome驱动
    web = webdriver.Chrome('D:\下载安装包文件\chromedriver.exe')
    #访问指定网页
    web.get('https://www.toutiao.com/ch/news_food/')
    #循环的值需要自己去设置，而且三个函数的循环次数要相同
    for i in range(1,1001):
        if i%50==0:
            time.sleep(30)
        try:
            #刷新网页获取更新后的内容
            web.refresh()
            time.sleep(1)
            #获取要抓取的网页部分源码
            b = BeautifulSoup(web.page_source,'lxml')
            part_crawl = b.select('.wcommonFeed')[0]
            #print(part_crawl)
            #将其放进列表中交给deal_part_crawl()函数进行处理
            Queue.put(part_crawl)
            time.sleep(0.5)
        except:
            pass

def deal_part_crawl():
    """该函数主要是用来处理将队列获得的信息进行过滤和清洗，获得有用的信息"""
    #设计正则表达式用于进行抓取新闻超链接
    pattern_link2 = r'<a class="link title" href="(.*?)" target="_blank">(.*?) </a>'
    for i in range(1000):
        #print(Queue.get())
        #从队列中获得内容
        try:
            part_crawl = Queue.get()
            #将内容转化为字符串进行正则匹配
            part_crawl_str = str(part_crawl)
            #print(part_crawl_str)
            link = re.compile(pattern_link2).findall(part_crawl_str) #正则匹配获得超链接列表
            #link1 = list(set(link)) #去掉重复的链接
            Queue2.put(link) #将列表放进另外一个队列中交给deal_link()函数进行处理
        except:
            pass

def deal_link():
    """该函数主要是用来将来自deal_part_crawl()函数的队列信息进行处理以获得完整的超链接并且超链接存进SQLite中"""
    # 创建sqlit3数据库
    conn = sqlite3.connect('toutiao_new.sqlite')
    cur = conn.cursor()
    cur.execute('create table if not exists Toutiao_food(Date varchar(100),title varchar(100),link varchar(100))')  # 创建数据表,表中信息有日期和超链接
    conn.commit()
    for i in range(1000):
        try:
            list_link = Queue2.get()
            for i in list_link:
                real_link = "https://www.toutiao.com"+i[0]
                #print(real_link)
                real_title = i[1]
                try:
                    cur.execute('insert into Toutiao_food values(?,?,?)',(time.ctime(),real_title,real_link))
                    conn.commit()
                except:
                    pass
        except:
            pass
    conn.close()
    print("储存完毕!")

    #list_only_link = list(set(list_only_link))
    #print(list_only_link)

#开启三条线程
t1 = threading.Thread(target=webopen)
t2 = threading.Thread(target=deal_part_crawl)
t3 = threading.Thread(target=deal_link)
t1.start()
t2.start()
t3.start()



