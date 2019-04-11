#1.时间间隔timedelta的扩展使用
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
now=datetime(2018,2,6)
print(now)

a=now+relativedelta(months=1)
print(a)

#2.进行差值月份统计
b=datetime(2018,1,2)
print(now-b)

d=relativedelta(now,b)
print(d)

print(d.months)
print(d.days)

#3.有关将字符串转为时间类型
text ='2018-02-06'
y=datetime.strptime(text,'%Y-%m-%d')
print(y)

def parse_ymd(s):
    year_s,mon_s,day_s=s.split('-')
    return datetime(int(year_s),int(mon_s),int(day_s))
k=parse_ymd(text)
print(k)

