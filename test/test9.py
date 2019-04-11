def power(x):
    return x*x
print(power(2))

def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(5,2))

def enroll(name,gender,age=6,city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age',age)
    print('city',city)
enroll('Sarah','F')

def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())

def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print(calc([1,2,3]))

def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print(calc(1,2))
nums=[1,2,3]
print(calc(*nums))

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
print(person('Michael',30))
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')

extra={'city':'Beijing','job':'Engineer'}
print(person('jack',24,**extra))

def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
print(person('jack',24,city="Beijing",addr='Chaoyang',zipcode=123456))

def person(name,age,*,city,job):
    print(name,age,city,job)
print(person('jack',24,city='beijing',job='Engineer'))

def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
print(f1(1,2))
print(f1(1,2,c=3))
print(f1(1,2,3,'a','b'))
print(f1(1,2,3,'a','b',x=99))
print(f2(1,2,d=99,ext=None))

args=(1,2,3,4)
kw={'d':99,'x':'#'}
print(f1(*args,**kw))
args=(1,2,3)
kw={'d':88,'x':'#'}
print(f2(*args,**kw))

def product(x,*y):
    for i in y:
        x=x*i
    return x
print(product(1,2,5,8))

