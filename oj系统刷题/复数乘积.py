b=[]
for i in range(2):
    x=input()
    a=x.split()
    b.append(a)
shi=int(b[0][0])*int(b[1][0])-int(b[0][1])*int(b[1][1])
xu=int(b[0][1])*int(b[1][0])+int(b[0][0])*int(b[1][1])
print(shi,xu)
