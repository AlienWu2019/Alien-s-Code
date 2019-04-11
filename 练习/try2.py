num = input("输入一个数字: ")
MOD = int(num)%2
if MOD>0:
    print("你选了一个奇数")
else:
    print("你选了一个偶数")


#-----------------------------
num = int(input("给我一个要检查的数字: "))
CHECK = int(input("给我一个数字除以: "))

if num%4==0:
    print(num,"是4的倍数")
elif num%2==0:
    print(num,"是偶数")
else:
    print(num,"是一个奇数")

if num%CHECK==0:
    print(num,"除以",CHECK)
else:
    print(num,"不均分",CHECK)
