#数学定理：假若p为质数，a为任意正整数，那么a^p-a可被p整除
import random
def feima():
    #产生一个随机的正整数
    a = random.randint(1,10000)
    #求2到1000的质数
    l=list(range(2,1000))
    for n,i in enumerate(l):
        for j in l[n+1:]:
            if j%i==0:
                l.remove(j)
    #将列表中的整数转化为字符串，目的是为了能取出单个质数
    for k in range(0,len(l)):
        l[k]=str(l[k])
    #把一个质数取出来
    r = "".join(random.sample(l,1))
    #将字符串类型的质数转化成int型进行运算判断
    p = int (r)
    if((a**p-a)%p==0):
        print("费马小定理得到验证！")
    else:
        print("费马小定理骗人的！")

feima()
