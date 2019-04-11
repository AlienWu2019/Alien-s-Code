import websocket

if __name__=="__main__":
    ws = websocket.create_connection('wss://tx-sh3-live-comet-01.chat.bilibili.com/sub',timeout=10)
    ws.send()
    while True:
        try:
            conncet = ws.recv()
            print(conncet)
        except:
            ws.send('2')
            continue