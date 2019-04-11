from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
from threading import Thread
import asyncio #尝试使用协程完成任务
from queue import Queue
import pymysql
import  time

q = Queue() #定义一个队列用于进行线程间的通讯
def get_all_music_table_Link():
    '''该函数主要是用于获取所有歌单的具体链接'''
    #把selenium设置为无窗口模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    op_web = webdriver.Chrome(r'D:\下载安装包文件\chromedriver.exe',options=chrome_options) #打开chrome驱动
    #迭代url获得1-35页的歌单
    page = 0 #初始页设置未0
    #定义url的格式
    url = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
    op_web.get(url) #启动selenium打开初始网页
    # 操作iframe，把当中有用的信息呈现
    op_web.switch_to.frame('g_iframe')
    while True:
        get_page_source = op_web.page_source  # 获得网页真实源码
        html = etree.HTML(get_page_source)  # 使用xpath采集下一页信息,以及每一页的歌单链接
        music_table_link = html.xpath('//p[@class="dec"]/a/@href') #数据类型为一个列表，列表中包含一页中每个所有歌单
        #print(music_table_link)
        q.put(music_table_link) #把html入列
        #print(get_page_source)
        click_next_page = '//div[@class="u-page"]/a[@class="zbtn znxt"]'#设置下一页的xpath
        try:
            op_web.execute_script("window.scrollTo(0, document.body.scrollHeight);") #拖动到页面最底部以定位到下一页按钮的位置
            op_web.find_element_by_xpath(click_next_page).click() #点击下一页
            time.sleep(1)
            # op_web.switch_to.default_content()
        except Exception as e:
            print(e)
            break
    #全部歌单链接采集完毕，关闭浏览器
    op_web.close()

def crawl():
    '''该函数主要是采集歌单的具体信息'''
    #再打开一个浏览器
    # 把selenium设置为无窗口模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    url_total = "https://music.163.com/#" #歌单标准头
    music_name_total = "https://music.163.com/#"
    #----------------------------
    '''连接mysql并且把数据存进mysql中'''
    conn = pymysql.connect("106.14.144.54", "root", "Wzl!13433627612","网易云音乐歌单")
    cur = conn.cursor()
    while True:
        # if q.empty()==True:  #判断队列是否为空
        #     break
        # else:
        try:
            url_list = q.get()
            for i in url_list:
                new_op_web = webdriver.Chrome(r'D:\下载安装包文件\chromedriver.exe', options=chrome_options)  # 打开chrome驱动
                table_url = url_total+i
                new_op_web.get(table_url) #打开歌单链接
                #操作iframe
                new_op_web.switch_to.frame('contentFrame')
                music_table_page_source = new_op_web.page_source #获得歌单源码
                data = etree.HTML(music_table_page_source) #利用xpath采集歌单信息
                music_table_name = data.xpath('//div[@class="tit"]/h2/text()') #采集歌单名字,list
                new_music_table_name=music_table_name[0].replace('\xa0','')
                play_times = data.xpath('//div[@class="more s-fc3"]/strong/text()') #采集播放次数,list
                tag = ','.join(data.xpath('//div[@class="tags f-cb"]/a[@class="u-tag"]/i/text()')) #采集标签变并且合并,str
                introduce = ''.join(data.xpath('//p[@id="album-desc-more"]/text()')) #采集介绍信息 str
                new_introduce = introduce.replace('\n','') #去掉\n
                music_link = data.xpath('//span[@class="txt"]/a/@href') #采集歌曲的链接list
                new_music_link = [] #完整歌曲url
                for i in music_link:
                    link = music_name_total+i
                    new_music_link.append(link)
                music_name = data.xpath('//span[@class="txt"]/a/b/@title') #采集歌曲名字list
                new_music_name = []  #去掉字符\xa0
                for ne in music_name:
                    new_music_name.append(ne.replace('\xa0',''))
                music_long = data.xpath('//td[@class=" s-fc3"]/span[@class="u-dur "]/text()') #采集歌曲时长 list
                author = data.xpath('//td[@class=""]/div[@class="text"]/span/@title') #采集作者名称list
                #把指定数据存进"歌单头"数据表中
                massage_head = (new_music_table_name,play_times[0],tag,new_introduce)
                print(massage_head)
                cur.execute('INSERT INTO `歌单头`(`music_table_name`, `play_times`, `tag`, `introduce`) VALUES {}'.format(massage_head))
                conn.commit()
                #把指定数据存进"歌单体"数据表中
                for yws in zip(new_music_name,new_music_link,music_long,author):
                    music_body = tuple([new_music_table_name]+[x for x in yws])
                    print(music_body)
                    cur.execute('INSERT INTO `歌单体` (`music_table_name`, `music_name`, `music_link`, `music_long`, `author`) VALUES {0}'.format(music_body)) #比较笨的一种实现方法，暂时没想到更好的办法
                    conn.commit()
                # print("歌单名:",music_table_name)
                # print("播放次数:",play_times)
                # print("标签:",tag)
                # print("介绍:",introduce)
                # print("歌曲链接:",music_link)
                # print("歌曲名:",music_name)
                # print("时长:",music_long)
                # print("作者",author)
                new_op_web.close() #采集完毕关闭浏览器
        except:
            print("数据全部采集完毕！")
            conn.close()


if __name__ =="__main__":
    t1 = Thread(target=get_all_music_table_Link)
    t2 = Thread(target=crawl)
    t1.start()
    t2.start()


















