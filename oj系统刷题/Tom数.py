for i in range(3):
    num = input()
    sum = 0
    if(int(num)<0):
        a1=int(num[0:2])
        sum+=a1
        for j in range(2,len(num)):
            sum+=int(num[j])
    else:
        for j in range(len(num)):
            sum+=int(num[j])
    print(sum)