import os

#如果该块中只有一条语句，则可以在同一行中指定它
if os.name == 'posix':
    print('You are cool')

def say_hello():
    return 'hello'

print(say_hello())

#清单理解
class Employee:
    def __str__(self):
        return self.name + str(self.salary)

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

employees = []
employees.append(Employee('Tom',30000))
employees.append(Employee('Satish',40000))
employees.append(Employee('Harry',50000))

#让我们列出工工资超过30000的所有员工的名单
#使用列表理解
sal_more_than_40k = [e for e in employees if e.salary >40000]
print("Listing " + str(len(sal_more_than_40k))+" employees with sal > 40K")
for emp in sal_more_than_40k:
    print(emp)

#现在让我们使用lambda表达式获得类似的内容
sal_more_than_30k = filter(lambda e : e.salary > 30000,employees)
print("Listing " + str(len(sal_more_than_30k)) + " employees with sal > 30k")
for emp in sal_more_than_30k:
    print(emp)

print(repr(sal_more_than_30k))
print(sal_more_than_30k)
eval(repr(sal_more_than_30k))
