from multiprocessing import Process,Pipe
import multiprocessing
import os

def aa(a):
    a.send('hello')
    print(os.getppid(),os.getpid())

def bb(b):
    b.send('hi')
    print(os.getppid(),os.getpid())

if __name__=="__main__":
    a_conn,b_conn = Pipe()
    p1 = Process(target=aa,args=(a_conn,))
    p1.start()
    p2 = Process(target=bb,args=(b_conn,))
    p2.start()

    data = b_conn.recv()
    print(data)
    kk = a_conn.recv()
    print(kk)