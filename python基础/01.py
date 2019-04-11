print('包含中文的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
x = b'ABC'
print(x)

print('ABC'.encode('ascii'))
print(b'ABC'.decode('ascii'))
print('中文'.encode('utf-8'))

print(len('ABC'))
print(len('中文'))
