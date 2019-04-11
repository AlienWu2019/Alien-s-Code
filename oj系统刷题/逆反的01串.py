for i in range(2):
    x=input()
    b=""
    for i in range(len(x)):
        if (x[i]=="0"):
            b=b+x[i].replace("0","1")
        elif (x[i]=="1"):
            b=b+x[i].replace("1","0")
    print(b)
