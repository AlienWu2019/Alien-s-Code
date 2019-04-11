import requests
from bs4 import BeautifulSoup
import sqlite3
import asyncio

class DGUToj:
    def __init__(self):
        # 创建数据库和表
        self.conn = sqlite3.connect('DGUToj.sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute(
            'create table if not exists DGUToj(title varchar(50),difficulty varchar(50),content varchar(50),content_in varchar(50),content_out varchar(50),Situation varchar(50))')
        self.conn.commit()

    async def oj_crawl(self):
        """抓取信息，并且清洗信息"""
        for i in range(1,1152):
            url = "http://oj.dgut.edu.cn/api/xproblem/{0}/".format(i)
            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
            }
            req = requests.get(url,headers=headers).json()
            #判断网页json是否找到
            if req['data'] != 'Not found.':
                # content=req['data']
                # print(content)
                #标题
                self.title = req['data']['title']
                #print(self.title)
                #题目难度
                self.difficulty = req['data']['difficulty']
                #print(self.difficulty)
                #题目内容
                self.content = BeautifulSoup(req['data']['description'],'lxml').text
                #print(self.content)
                #输入
                self.content_in = BeautifulSoup(req['data']['input_description'],'lxml').text
                #print(self.content_in)
                #输出
                self.content_out = BeautifulSoup(req['data']['output_description'],'lxml').text
                #print(self.content_out)
                #作答情况
                self.s=""
                self.staus = req['data']['statistic_info']
                for key in self.staus:
                    if key == '0':
                        self.s += '正确:' + str(self.staus['0']) + ','
                    elif key == '1':
                        self.s += '超出时间限制:' + str(self.staus['1']) + ','
                    elif key == '4':
                        self.s += '运行错误:' + str(self.staus['4']) + ','
                    elif key == '-1':
                        self.s += '答案错误:' + str(self.staus['-1']) + ','
                    elif key == '-2':
                        self.s += '编译错误:' + str(self.staus['-2']) + ','
                self.s = self.s[:-1] #把作答情况字符串末尾的','去掉
                await self.insertSql()
        self.conn.close()


    async def insertSql(self):
        """将数据存到sqlite数据库中"""
        try:
            self.cur.execute('insert into DGUToj values(?,?,?,?,?,?)',(self.title,self.difficulty,self.content,self.content_in,self.content_out,self.s))
            self.conn.commit()
        except:
            pass

if __name__=="__main__":
    """实例化"""
    c = DGUToj()
    asyncio.run(c.oj_crawl())
    print("采集完毕!")