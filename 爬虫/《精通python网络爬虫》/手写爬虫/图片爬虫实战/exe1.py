import re
import urllib.request

def craw(url,page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+ <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width="220" height="220" data-img="1" (.*?)">'
    imagelist = re.compile(pat2).findall(result1)
    imagelist_new=[]
    for i in imagelist:
        if i[0]=="s":
            imagelist_new.append(i[7:])
        elif i[0]=="d":
            imagelist_new.append(i[17:])
    x=1
    for imageurl in imagelist_new:
        print(imageurl)

        imagename = "C:/Users/58294/Documents/Python File/picture/"+str(page)+str(x)+".jpg"
        imageurl = "https://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.request.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1


for i in range(1,43):
     url = "https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
     craw(url,i)
print("大功告成！")