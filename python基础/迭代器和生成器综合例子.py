list1 = [1,2,3,4,5]
for num1 in list1:
    print(num1,end = ' ')

print('\n---------------------')
#反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。 如果两者都不符合，那你必须先将对象转换为一个列表才行
list2 = [1,2,3,4,5]
for num2 in reversed(list2):
    print(num2,end= ' ')

print('\n---------------------')

class Countdown:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        #Forward iterator
        n = self.start
        while n>0:
            yield n
            n -= 1

    def __reversed__(self):
        #Reverse iterator
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)
print('-------------')
for rr in Countdown(30):
    print(rr)

print('\n---------------------')
#同时迭代多个序列
names = ['liangdianshui','twowater','两点水']
ages = [18,19,20]
for name,age in zip(names,ages):
    print(name,age)

print('\n---------------------')

names = ['liangdianshui','twowater','两点水']
ages = [18,19,20]

dict1 = dict(zip(names,ages))
print(dict1)
