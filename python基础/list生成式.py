list1 = list( range (1,31))
print(list1)

print('------------------------------\n')

print('\n'.join([' '.join('%d*%d=%d' % (x,y,x*y) for x in range(1,y+1)) for y in range(1,10)]))

print('-------------------------------\n')

list2 = [x*x for x in range(1,11)]
print(list2)

print('-------------------------------\n')

list3 = [x*x for x in range(1,11) if x %2 ==0]
print(list3)
