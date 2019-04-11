while True:
    a=input()
    x=a.split()
    if a=='EOF':
        break
    elif 0>=int(x[0])or 0>=int(x[1]) or int(x[0])>20 or int(x[1])>20 or int(x[0])<int(x[1]):
        break
    else:
        sum=1
        temp1=int(x[0])
        temp2=1
        for i in range(int(x[1])):
            sum=sum*temp1
            temp1=temp1-1
            temp2=temp2*(i+1)
        print(int(sum/temp2))
