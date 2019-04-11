power2 = []
for i in range (1,10):
    power2.append(i*i)
print(power2)

squares = [x**2 for x in range (1,10)]
print(squares)

def a():
    L = []
    for x in range(0,100):
        if x % 3 == 0:
            L.append(x)
    print(L)

a()

L = [n for n in range(0,100) if n %3 == 0]
print(L)


