a = int(input("请您输入一个数字: "))
b=[]
for i in range(1,a+1):
    if a % i ==0:
        b.append(i)
print("该数的所有除数列表是:",b)
