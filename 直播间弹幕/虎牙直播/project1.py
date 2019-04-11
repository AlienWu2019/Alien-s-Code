from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sqlite3

class huyaDanmu:
    def __init__(self,url):
        self.url = url
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.broswer = webdriver.Chrome(r'D:\下载安装包文件\chromedriver.exe',options=chrome_options)
        self.broswer.get(self.url)
        # 创建sqlite数据库用于存储弹幕内容
        # self.conn = sqlite3.connect('Danmu.sqlite')
        # self.cur = self.conn.cursor()
        # self.cur.execute(
        #     'create table if not exists HuyaDanmu (Date varchar(20),content varchar(100));')
        # self.conn.commit()

    #启动浏览器打开指定直播间
    def startdriver(self):
        count=1
        while True:
            try:
                get_danmu = self.broswer.find_elements_by_xpath('//li[@class="J_msg"]') #获得弹幕内容
                #print(len(get_danmu)) #一直等待有新的弹幕,一次获取的弹幕数量未知
                l = len(get_danmu) - count #l为需要打印的弹幕数量
                if l < 0:
                    count = 0
                    continue
                elif l == 0:
                    continue
                for i in range(l):
                    result = get_danmu[-1 * l:].pop(i) #把弹幕推出栈内
                    #对弹幕进行清洗
                    print(result.text)
                    count += 1    #每推出一条弹幕，计数加1
                if len(get_danmu)==100:
                    self.broswer.refresh()
                    count=0
            except Exception as e:
                print(e)
                pass
            #处理弹幕
            # try:
            #     userName,msg = get_danmu.split(':')
            #     print(userName,'说:',msg)
            # except:
            #     pass
            # self.deal_danmu()
            # 缓冲一下，尽量减少重复弹幕处理

    # #处理弹幕内容，并将其存进数据库中
    # def deal_danmu(self):
    #     for i in range(len(self.list_danmu_deal)):
    #         try:
    #             if self.list_danmu_deal[i] == ':':
    #                 insert = (time.ctime(),self.list_danmu_deal[:i],self.list_danmu_deal[i+1:])
    #                 print(insert)
    #                 self.cur.execute('insert into HuyaDanmu values(?,?,?)',insert)
    #                 self.conn.commit()
    #         except:
    #             pass


a = huyaDanmu('https://www.huya.com/lafeng')
a.startdriver()







