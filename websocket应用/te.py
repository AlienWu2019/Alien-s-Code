import requests
import json
import websocket
he={
'Accept': '*/*',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Origin': 'http://www.dooccn.com',
'Referer': 'http://www.dooccn.com/c/'
}
datas = {
'language': '18',
'code': 'PD9waHAKJGRhdGEgPSAneyJyb29tSWQiOjEwMjQxMX0nOwokdGltZSA9IHRpbWUoKTsKaWYoJGRhdGEpewogICAgJHN0ciA9ICRkYXRhOwp9ZWxzZXsKICAgICRzdHIgPSAnIiInOwp9CiRzaWduID0gbWQ1KCJkYXRhPXskc3RyfSZrZXk9NzEwY2RjZjkmdGltZXN0YW1wPXskdGltZX0iKTsKZWNobygkc2lnbik7CmVjaG8oJHRpbWUpOwo/Pg==',
}

req = requests.post("http://runcode-api2-ng.dooccn.com/compile2",data=datas,headers=he).text
print(req)
data = json.loads(req)
sign = data["output"][:32]
print(sign)
t = data["output"][32:]
print(t)

appID = '155478987827019346'
secretld = "710cdcf9"
ws = websocket.create_connection('wss://openapi.huya.com/index.html?do=getMessageNotice&data={"roomId":102411}&appId=155478987827019346&timestamp=%s&sign=%s'%(t,sign))
ws.send('ping')
i=0
while True:
    try:
        print(ws.recv())
        i+=1
        if i%10==0:
            ws.send('ping')
    except:
        ws.send('ping')