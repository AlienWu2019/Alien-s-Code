import time
import hashlib
def foo():
    a= int(time.time()*10**3)
    t = int(a/1000)
    e = str(hex(t)).upper()[2:]
    #print(e)
    i=str(hashlib.md5(bytes(str(t),encoding='utf-8')).hexdigest()).upper()
    #print(i)
    if len(e) !=8:
        return {"as":"479BB4B7254C150","cp":"7E0AC8874BB0985"}
    else:
        s=""
        r = ""
        for o in range(5):
            n = i[0:5]
            #print("n",n)
            a = i[-5:]
            #print("a", a)
            s +=n[o]+a[o]
        for c in range(5):
            r += e[c+3] +a[c]
        a1 = "A1"+s+e[-3:]
        c1 = e[0:3]+r+"E1"
        return (a1,c1)
a,b = foo()
print(a,b)








