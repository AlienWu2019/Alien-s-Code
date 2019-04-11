x=int(input())
if(x==2):
    print(1)
elif(x<2):
    print(0)
else:
    for i in range(2,x):
        if(x%i==0):
            print(0)
            break
    else:
        print(1)
