import random
def caiquan():
    a=['剪刀','石头','布']
    while True:
        Mike=''.join(random.sample(a,1))
        John=''.join(random.sample(a,1))
        print('Mike出了',Mike)
        print('John出了',John)
        if(Mike==John):
            print('两人平手，重新开始！')
        elif(Mike=='剪刀'and John=='布' or Mike=='石头' and John=='剪刀' or Mike=='布' and John=='石头'):
            print('Mike赢了！')
            break
        else:
            print('John赢了！')
            break

caiquan()
