import websocket
import json
'''           [object Object]'''

if __name__=="__main__":
    ws  = websocket.create_connection('wss://tx-gz3-live-comet-05.chat.bilibili.com/sub',timeout=10)
    ws.send(json.dumps('   b        {"uid":0,"roomid":5279,"protover":2,"platform":"web","clientver":"1.6.3","type":2}'))
    print(ws.recv())
