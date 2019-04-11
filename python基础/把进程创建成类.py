import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    def __init__(self,interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n=5
        while n>0:
            print("当前时间: {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
