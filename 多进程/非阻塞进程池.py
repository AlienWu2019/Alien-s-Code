import multiprocessing
import time

def test(msg):
    """定义一个函数测试线程池"""
    print('start',msg)
    time.sleep(1)
    print('end',msg)

if __name__=="__main__":
    #创建进程池,进程池里面有3个进程
    mp = multiprocessing.Pool(processes=3)
    for i in range(3):
        mp.apply_async(test,(i,)) #进程非阻塞的原因
    print('mark')
    mp.close() #关闭进程池，若没关闭的话程序会报错：Pool is still running
    mp.join()
    print('endmark')
