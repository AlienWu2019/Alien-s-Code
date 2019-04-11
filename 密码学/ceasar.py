from operator import mod
#ceasar加密算法
def ceasarC(a):
    L=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']#把英文字母和十进制数字的对应关系存进一个数组中
    s=list(a)#把字符串a变成字符数组
    p=[]
    for k in s:#逐个遍历s中的元素
        m=L.index(k)#找到数组s中元素k对应数组L中的位置
        #进行ceasar加密
        if m>=0 and m<=23:
           c=mod(m+3,26)
           p.append(L[c])
        elif m>23:
           c=mod(25-m,26)
           p.append(L[c])
    str1=''.join(p)
    print(str1)
print('Ceasar加密:')
ceasarC('iloveyou')
print('--------------------------------------------------')
print('--------------------------------------------------')
def ceasarM(b):
    L=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']#把英文字母和十进制数字的对应关系存进一个数组中
    s=list(b)
    p=[]
    for k in s:
        x=L.index(k)
        if x<2:
            m=mod(23+x,26)
            p.append(L[m])
        elif x>=2 and x<=25:
            m=mod(x-3,26)
            p.append(L[m])
    str2=''.join(p)
    print(str2)
print('Ceasar解密:')
ceasarM('loryhbrx')


