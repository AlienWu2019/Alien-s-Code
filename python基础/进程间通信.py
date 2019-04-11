from multiprocessing import Process,Queue
import os,time,random

def write(q):
    #写数据进程
    print('写进程的PID： {0}'.format(os.getpid()))
    for value in ['两点水','三点水','四点水']:
        print('写进Queue 的值为: {0}'.format(value))
        q.put(value)
        time.sleep(random.random())

def read(q):
    #读取数据进程
    print('读进程的PID： {0}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('从Queue读取的值为: {0}'.format(value))

if __name__ == '__main__':
    #父进程创建Queue,并传给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动子进程pw
    pw.start()
    #启动子进程pr
    pr.start()
    #等待pw结束：
    pw.join()
    ##pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()
