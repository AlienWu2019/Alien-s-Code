from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('进程名称: {0} ; 进程的PID：{1} '.format(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('进程 {0} 运行了 {1} 秒'.format(name,(end-start)))

if __name__ == '__main__':
    print('主进程的PID： {0}'.format(os.getpid()))
    p = Pool(6)
    for i in range(6):
        p.apply_async(long_time_task,args=(i,))
    p.close()  #执行join前要先只想close，不然会不断创建子进程
    #等待所有主进程结束后再关闭主进程
    p.join()
    print('【END】')
