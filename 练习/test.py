import redis

r = redis.Redis("127.0.0.1",port=6379,db=0)

r.lpush("bilibili:start_urls","https://api.bilibili.com/x/space/acc/info?mid=1&jsonp=jsonp")
