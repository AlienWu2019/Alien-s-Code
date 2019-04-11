import requests
import time
import hashlib

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}

#获得as，cp
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

a,c = foo()

url = 'https://www.toutiao.com/api/pc/feed/?category=news_entertainment&utm_source=toutiao&widen=1&max_behot_time={0}&max_behot_time_tmp={1}&tadrequire=true&as={2}&cp={3}'.format(int(time.time()),int(time.time()),a,c)

print(url)

req = requests.get(url,headers=headers).text.encode('ascii').decode('unicode_escape')

print(req)