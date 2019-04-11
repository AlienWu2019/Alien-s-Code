from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
from queue import Queue
import threading
import pymysql

q = Queue()
# conn_mysql = pymysql.connect("106.14.144.54","root","Wzl!13433627612","网易云音乐")
# cur = conn_mysql.cursor()
id={'飙升榜':19723756,'新歌榜':3779629,'原创榜':2884035,'热歌榜':3778678,'江小白YOLO说唱榜':991319590,'以团之名发光榜':2629421353,'古典音乐榜':71384707,'电音榜':1978921795,'抖音榜':2250011882,'ACG音乐榜':71385702,'韩语榜':745956260,'国电榜':10520166,'英国Q杂志中文版周榜':2023401535,'电竞音乐榜':2006508653,'UK排行榜周榜':180106,'美国Billboard周榜':60198,'Beatport全球电子舞曲榜':3812895,'法国NRJ周榜':27135204,'KTV唛榜':21845217,'iTunes榜':11641012,'日本Oricon周榜':60131,'HitFMTop榜':120001,'台湾Hito榜':112463,'香港电台中文歌曲龙虎榜':10169002,'新声榜':2617766278}

def get_PageSource(uid):
    '''爬取榜单歌曲信息'''
    url_biaosheng = 'https://music.163.com/#/discover/toplist?id={0}'.format(uid) #飙升榜的url
    #设计chrom无窗口模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    #启动chromedirver,为无窗口后台模式
    op_chrome = webdriver.Chrome(r'D:\下载安装包文件\chromedriver.exe',options=chrome_options)
    #打开网页
    op_chrome.get(url_biaosheng)
    op_chrome.switch_to.frame("contentFrame") #切换到iframe <iframe>(html)</iframe>  html嵌套html为一个整体
    #休眠两分钟等待js渲染完毕
    # time.sleep(2)
    #获取网页的完全体源代码
    html = op_chrome.page_source   #type ->str
    #关闭浏览器
    op_chrome.close()
    #print(html)
    q.put((html,uid)) #多线程队列通讯

def music_Deatil():
    '''获取该榜中的歌曲并且排名'''
    # print(get_PageSource(id))
    data,uid = q.get()
    html = etree.HTML(data)
    #rank = html.xpath('//tbody/tr[@*]/td/div[@class="hd"]/span[@class="num"]/text()') #歌曲排名列表
    music_name = html.xpath('//div[@class="ttc"]/span[@class="txt"]/a[@*]/b/@title')
    music_name_newslist=[]#歌曲名称
    for i in music_name:
        music_name_newslist.append(str(i).replace('\xa0',' '))
    music_link = html.xpath('//div[@class="ttc"]/span[@class="txt"]/a/@href')
    music_link_newlist=[] #歌曲超链接
    for i in music_link:
        new_link = "https://music.163.com/#"+i
        music_link_newlist.append(new_link)
    music_long = html.xpath('//td[@class=" s-fc3"]/span[@class="u-dur "]/text()') #歌曲时长
    music_author = html.xpath('//td[@class=""]/div[@class="text"]/@title') #歌曲作者
    author_link = html.xpath('//td[@class=""]/div[@class="text"]/span[@*]/a[@hidefocus="true"]/@href')
    author_link_newlist=[] #作者个人主页
    for i in author_link:
        author_new_link = "https://music.163.com/#"+i
        author_link_newlist.append(author_new_link)
    conn_mysql = pymysql.connect("106.14.144.54", "root", "Wzl!13433627612", "网易云音乐")
    cur = conn_mysql.cursor()
    for j in zip(music_name_newslist,music_link_newlist,music_long,music_author,author_link_newlist):
        #print(j)
        print(list(id.keys())[list(id.values()).index(uid)])
        print(type(list(id.keys())[list(id.values()).index(uid)]))
        try:
            cur.execute("INSERT INTO `{0}` (`music_name`, `music_link`, `music_time`, `author`, `author_link`) VALUES {1}".format(list(id.keys())[list(id.values()).index(uid)],j))
            conn_mysql.commit()
        except Exception as e:
            print(e)
            conn_mysql.close()
    conn_mysql.close()



if __name__=='__main__':
    '''id = 19723756,3779629,2884035,3778678,991319590,2629421353,71384707,1978921795,2250011882,71385702,745956260,10520166,2023401535,2006508653,180106,60198,3812895,27135204,21845217,11641012,60131,120001,112463,10169002,2617766278'''
    for i in id.values():
        t1 = threading.Thread(target=get_PageSource,args=(i,)) #args以元组形式传入实参
        t2 = threading.Thread(target=music_Deatil)
        t1.start()
        t2.start()


