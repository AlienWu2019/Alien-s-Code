from multiprocessing import Process
import os
from time import sleep

def run():
    while True:
        print('进程id是:',os.getpid(),'  父进程id是:',os.getppid())
        sleep(1)


if __name__=='__main__':
    p = Process(target=run)
    p.start()
    while True:
        print('当前进程id：',os.getpid())
        sleep(1)