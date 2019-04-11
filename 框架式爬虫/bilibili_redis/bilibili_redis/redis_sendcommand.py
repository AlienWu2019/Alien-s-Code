import redis
import time
import random

r = redis.Redis("106.14.144.54",port=6379,db=0,password="root")
i=75600
times=[10.11,20.22,30.33]
while True:
    if r.llen("bilibili:start_urls")<=20:
        r.lpush("bilibili:start_urls","https://api.bilibili.com/x/space/acc/info?mid={0}&jsonp=jsonp".format(i))
        i+=1
    else:
        time.sleep(random.choice(times))


