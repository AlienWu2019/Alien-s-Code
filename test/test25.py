import time; #引入time模块

ticks = time.time()
print("当前时间截至为:",ticks)

localtime = time.localtime(time.time())
print("本地时间为: ",localtime)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为: ",localtime)

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

print(time.strftime("%a %b %c %H:%M:%S %y",time.localtime()))

