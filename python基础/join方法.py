import multiprocessing
import time

def worker(interval):
    print('工作开始时间: {0}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结果时间: {0}'.format(time.ctime()))


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker,args=(3,))
    p.daemon = True
    p.start()
    p.join()
    print('【EMD】')
