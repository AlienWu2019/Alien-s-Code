import redis

r = redis.Redis('127.0.0.1',port=6379,db=0)
r.set('myname','alien')
print(r.get('myname'))
