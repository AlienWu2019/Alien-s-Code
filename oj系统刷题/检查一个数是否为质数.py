x=int(input())
if(x<2):
    print('N')
elif(x==2):
    print('Y')
else:
    for i in range(2,x):
        if(x%i==0):
            print('N')
            break
    else:
        print('Y')
