import base64
s = '我是字符串'.encode()
a = base64.b64encode(s)
print(a)