def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
print(fact(5))

def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        '''把n-个汉诺塔绕过c放到b上'''
        print(a,'-->',c)
        move(n-1,b,a,c)
        '''把n-1个汉诺塔绕过a放到c上'''
print(move(3,'A','B','C'))


