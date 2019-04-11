from multiprocessing import Process
import time
import os

def test(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == "__main__":
    print("当前进程:",os.getpid())
    pl = []
    for i in range(5):
        p = Process(target=test,args=(1,))
        p.start()
