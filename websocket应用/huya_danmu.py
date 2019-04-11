import websocket
import base64
import requests
import json

class Huya_Danmu:
    def __init__(self,roomID):
        '''初始化api所需的参数'''
        self.roomID = str(roomID) #str
        self.appID = '155478987827019346' #str
        self.secretld = "710cdcf9"
        self.header = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://www.dooccn.com',
            'Referer': 'http://www.dooccn.com/c/'
        }

    def get_sign(self):
        '''获得sign参数'''
        #编写php代码
        php_code='''<?php
$data = '{"roomId":%s}';
$time = time();
if($data){
    $str = $data;
}else{
    $str = '""';
}
$sign = md5("data={$str}&key=710cdcf9&timestamp={$time}");
echo($sign);
echo($time);
?>'''%(self.roomID)
        base64_php_code = str(base64.b64encode(php_code.encode('utf-8')),'utf-8')
        datas = {
            'language': '18',
            'code': base64_php_code,
        }
        req = requests.post("http://runcode-api2-ng.dooccn.com/compile2",data=datas,headers=self.header).text
        req_json = json.loads(req)
        sign = req_json["output"][:32]
        t = req_json["output"][32:]
        #print(sign)
        #print(t)
        return sign,t

    def get_danmu(self):
        '''获得弹幕内容'''
        s,t = self.get_sign()
        ws = websocket.create_connection('wss://openapi.huya.com/index.html?do=getMessageNotice&data={"roomId":%s}&appId=%s&timestamp=%s&sign=%s'%(self.roomID,self.appID,t,s))
        ws.send('ping')
        i=0
        while True:
            try:
                msg=ws.recv()
                sendNick = json.loads(msg)["data"]["sendNick"] #用户名
                content = json.loads(msg)["data"]["content"]
                print(sendNick,":",content) #打印弹幕
                i+=1
                if i%15==0:
                    ws.send('ping') #websocket心跳检测
            except:
                continue


if __name__=="__main__":
    roomid = input("请输入直播间的房间号:")
    dm = Huya_Danmu(roomid)
    dm.get_danmu()