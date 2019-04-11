while(True):
    x=[]
    a=input()
    b=a.split(' ')
    if(len(b)>10):
        print("超出范围，请重试!")
        continue
    else:
        for i in range(len(b)):
            x.append(int(b[i].strip()))
        x=list(set(x))
        x.sort()
        for j in range(len(x)):
            print(x[j])
        break

