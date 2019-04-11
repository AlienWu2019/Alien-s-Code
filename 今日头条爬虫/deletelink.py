import sqlite3

def conn_sql():
    # 连接sqlite将数据库中的连接取出来
    conn = sqlite3.connect('toutiao.sqlite')
    cur = conn.cursor()
    select_link = cur.execute('select * from toutiao_caijing')
    link_list=[]
    for link in select_link:
        link_list.append(link[1])
    return link_list
for i in conn_sql():
    print(i)

