n=input("请输入你的大名:")
print('您好!',n)
s=input('您的出生年份:')
birth=int(s)
if birth< 2000:
    print('您是00前的哲学家')
else:
    print('您是00后的哲学家')
a=input('您的体身高是:')
high=float(a)
b=input('您的体重是:')
weigth=float(b)
BMI=weigth/(high*high)
if BMI<18.5:
    print(n,'您过轻!')
elif BMI>=18.5 and BMI<25:
    print(n,'您正常!')
elif BMI>=25 and BMI<28:
    print(n,'您过重!')
elif BMI>=28 and BMI<32:
    print(n,'您肥胖!')
else:
    print(n,'您严重肥胖!')
