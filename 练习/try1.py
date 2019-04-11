import time
name = input("请您输入姓名：")
age = input("请您输入年龄: ")
print('---------------------------')
print("您的名字是："+name)
print("您的年龄是: "+age)
a = int(time.strftime('%Y',time.localtime()))+100-int(age)
man = str(a)
print(name+"将在"+man+"年满100周岁！")
