import calendar
a=input()
b=a.split()
y=int(b[0])
m=int(b[1])
if(y>=2007):
    print(calendar.month(y,m))
