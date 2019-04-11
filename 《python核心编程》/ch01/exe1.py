from random import randrange,choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ('com','edu','net','org','gov')

for i in range(randrange(5,11)): #randrange(5,11):5到11范围内随机一个数,默认递增基数为1
    dtint = randrange(2**32)
    dtstr = ctime(dtint)  #从1970年开始以秒数开始计算
    llen = randrange(4,7)
    # choice()方法返回一个列表，元组或字符串的随机项。lc:26个小写英文字符随机排序
    login = ''.join(choice(lc) for j in range(llen)) #生成一个无序长度不一样的字符串组
    dlen = randrange(llen,13)
    dom = ''.join(choice(lc) for k in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d'%(dtstr, login,
        dom, choice(tlds), dtint, llen, dlen))

