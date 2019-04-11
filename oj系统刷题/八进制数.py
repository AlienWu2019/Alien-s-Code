import sys
for i in range(10):
    x=int(input())
    if(0<=x<=100000):
        print("%o" %x)
    else:
        sys.exit()
