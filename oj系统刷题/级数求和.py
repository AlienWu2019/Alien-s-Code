K=int(input())
Sn=0
if(1<=K<=15):
    for n in range(1,10000000):
        Sn=Sn+1/n
        if(Sn>K):
            print(n)
            break
