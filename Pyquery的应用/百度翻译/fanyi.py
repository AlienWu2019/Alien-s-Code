import requests
import json

class fanyi:
    def __init__(self,keyword):
        self.keyword = keyword

    def result(self):
        url = "https://fanyi.baidu.com/extendtrans"
        # 设置提交数据
        posData = {"query": self.keyword,
                   "from": "en",
                   "to": "zh"}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36'
        }
        req = requests.post(url,posData,headers=headers)
        json_data = json.loads(req.content.decode())

        # 然后我们可以通过格式化工具进行json的解析
        return ','.join(json_data["data"]["st_tag"])


if __name__=="__main__":
    keyword = input()
    a = fanyi(keyword)
    print(a.result())
