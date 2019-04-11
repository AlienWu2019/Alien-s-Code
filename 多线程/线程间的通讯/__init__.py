from queue import Queue
from threading import Thread
import random
import time

_sentinel = object()

def producer(out_q):
    n=10
    while n:
        time.sleep(1)
        data = random.randint(0,10)
        out_q.put(data)
        print("生产者生产了数据{0}".format(data))
        n-=1
    out_q.put(_sentinel)

def consumer(in_q):
    while True:
        data = in_q.get()
        print("消费者消费了{0}".format(data))
        if data is _sentinel:
            in_q.put(_sentinel)
            break

q= Queue()
t1 = Thread(target=producer,args=(q,))
t2 = Thread(target=consumer,args=(q,))

t1.start()
t2.start()