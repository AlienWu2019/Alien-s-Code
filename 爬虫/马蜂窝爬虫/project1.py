import sqlite3

conn = sqlite3.connect('test3.sqlite')
cur = conn.cursor()
cur.execute("create table if not exists bilibili(title varchar(100),content varchar(100))")
conn.commit()
for t in[('为什么传统刺客打野一直比赛上不是最优选择？', '没有内容'),('高渐离现在可以拿出来用了', '没有内容')]:
    cur.execute("insert into bilibili values (?,?)", t)
conn.commit()
conn.close()

