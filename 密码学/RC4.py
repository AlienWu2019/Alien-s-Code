from Crypto.Cipher import AES
#秘钥,此处需要将字符串转为字节
key = b'abcdefgh'
#加密内容需要长达16位字符，所以进行空格拼接
def pad(text):
    while len(text) % 16 != 0:
        text += b' '
    return text
#加密秘钥需要长达16位字符，所以进行空格拼接
def pad_key(key):
    while len(key) % 16 != 0:
        key += b' '
    return key
#进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
aes = AES.new(pad_key(key), AES.MODE_ECB)
#加密内容,此处需要将字符串转为字节
text = b'woshijiamineirong'
#进行内容拼接16位字符后传入加密类中，结果为字节类型
encrypted_text = aes.encrypt(pad(text))
print(encrypted_text)


#此处是为了验证是否能将字节转为字符串后，进行解密成功
#实际上a 就是 encrypted_text ，也就是加密后的内容
a = b'\xb9K\xe8_.q\x1c!\x9f\xa2\xc8\x06\xf5\xc1\xd07'
#用aes对象进行解密，将字节类型转为str类型，错误编码忽略不计
de = str(aes.decrypt(a),encoding='utf-8',errors="ignore")
#获取str从0开始到文本内容的字符串长度。
print(de[:len(text)])
