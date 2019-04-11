import requests
import pymysql
import re

#连接数据库：
db = pymysql.connect("localhost","root","root","search_news",charset='utf8')

while True:
    info = input("输入对话内容:")
    cur = db.cursor()
    if info == "exit":
        sql = "select * from news"
        try:
            cur.execute(sql)
            results = cur.fetchall()
            print("内容是:",results)
        except Exception as e:
            raise e
        exit()
    else:
        appkey = "e5ccc9c7c8834ec3b08940e290ff1559"
        url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
        search_str = '{"code":.*?,"text":"(.*?)"}'
        req = requests.get(url).text
        content = req
        search_content = re.compile(search_str)
        result_news = search_content.findall(content)
        str_result_news = "".join(result_news)
        print(str_result_news)
        sql_insert = "insert into news (content) values ('{0}')".format(str_result_news)
        try:
            cur.execute(sql_insert)
            #提交
            db.commit()
        except Exception as e:
            #错误回滚
            db.rollback()




