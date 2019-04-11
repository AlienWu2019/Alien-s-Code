from string import ascii_lowercase as lc
from random import randrange,choice
import threading
from time import ctime
from multiprocessing import Process
import time

def t1():
    tlds = ('com', 'edu', 'net', 'org', 'gov')
    print("this is func(t1):")
    for i in range(randrange(5, 11)):  # randrange(5,11):5到11范围内随机一个数,默认递增基数为1
        dtint = randrange(2 ** 32)
        dtstr = ctime(dtint)  # 从1970年开始以秒数开始计算
        llen = randrange(4, 7)
        # choice()方法返回一个列表，元组或字符串的随机项。lc:26个小写英文字符随机排序
        login = ''.join(choice(lc) for j in range(llen))  # 生成一个无序长度不一样的字符串组
        dlen = randrange(llen, 13)
        dom = ''.join(choice(lc) for k in range(dlen))
        print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,dom, choice(tlds), dtint, llen, dlen))
        time.sleep(2)

def t2():
    tlds = ('com', 'edu', 'net', 'org', 'gov')
    print("this is func(t2):")
    for i in range(randrange(5, 11)):  # randrange(5,11):5到11范围内随机一个数,默认递增基数为1
        dtint = randrange(2 ** 32)
        dtstr = ctime(dtint)  # 从1970年开始以秒数开始计算
        llen = randrange(4, 7)
        # choice()方法返回一个列表，元组或字符串的随机项。lc:26个小写英文字符随机排序
        login = ''.join(choice(lc) for j in range(llen))  # 生成一个无序长度不一样的字符串组
        dlen = randrange(llen, 13)
        dom = ''.join(choice(lc) for k in range(dlen))
        print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,dom, choice(tlds), dtint, llen, dlen))


# th = threading.Thread(target=t1)
# th1 = threading.Thread(target=t1)
# th.start()
# th.join()
# th1.start()
if __name__ == "__main__":
    p1 = Process(target=t1)
    p2 = Process(target=t2)
    p1.start()
    p1.join() #就算p1运行的慢，但是还是得阻塞掉p2进程，让p1完全执行完了才执行p2，这样得话就能够有顺序的执行了
    p2.start()
