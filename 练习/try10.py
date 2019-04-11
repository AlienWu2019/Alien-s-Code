a=int(input("请输入一个数："))
if(a==1):
    print("1既不是素质也不是合数！")
elif(a==2):
    print("这是素数！")
else:
    for i in range(2,a):
        if(a%i==0):
            print("这个数是合数！")
            break
#大意是说当迭代的对象迭代完并为空时，位于else的子句将执行，而如果在for循环中含有break时则直接终止循环，并不会执行else子句
    else:
        print("这个数是质数！")



