N=int(input())
a=[3,4,5]
for i in range(N-3):
    a.append(a[i]+a[i+1]+a[i+2])
print(a[-1])