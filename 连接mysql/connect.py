import pymysql

#打开数据库连接
db = pymysql.connect("localhost","root","root","project")
#创建游标对象
cur = db.cursor()
#查询操作
sql = "select * from user"
try:
    cur.execute(sql)  #执行sql语句
    result = cur.fetchall()  #获取查询的所有数据
    print("userName"," password","name"," sex","birth")
    for row in result:
        userName = row[0]
        password = row[1]
        name = row[2]
        sex = row[3]
        birth = row[4]
        print(userName,password,name,sex,birth)

except Exception as e:
    raise e
finally:
    db.close()
