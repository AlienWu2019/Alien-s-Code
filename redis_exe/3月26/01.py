import redis

#创建redis连接
r = redis.Redis("106.14.144.54",port=6379,db=0,password="root")
'''set()'''
r.set('name','zhangsan') #不会过期，一直在redis中
#r.setex('name',10,'lisi') #设置过期时间(秒)，过期之后键值对从redis中消失
#r.psetex('name',100,'wuwu') #设置过期时间(毫秒)

'''mset()'''
r.mset({'name1':'lii','name2':'rr'}) #批量设置值
#get(name)获取值
print(r.mget('name1','name2')) #批量获取

#getset()设置新值，打印原值
print(r.getset('name1','ttrr')) #输出lii
print(r.get('name1')) #输出ttrr

#getrange(key,start,end)根据字节获取子序列
print(r.getrange('name1',0,2)) #输出ttr

#setrange()修改字符串内容，从指定字符串索引开始向后替换，如果新值太长时，则向后添加
print(r.setrange('name1',1,'o')) #输出torr


