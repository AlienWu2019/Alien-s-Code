x=int(input())
a=input()
a_list=a.split()
num=int(input())
str_1=input()
str_1_list=str_1.split()
if len(a_list)==x and len(str_1_list)==num and num<=x:
    for i in range(len(str_1_list)):
        if str_1_list[i] in a_list:
            print('YES')
        else:
            print('NO')




