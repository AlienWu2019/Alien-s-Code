#
# "https://www.toutiao.com/api/pc/feed/?category=news_game&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1955CD847FAEBE&cp=5C871A8E6BAE8E1&_signature=RnjCQwAAGwHsV4LDHvU8ykZ4wl"
#
# "https://www.toutiao.com/api/pc/feed/?category=news_game&utm_source=toutiao&widen=1&max_behot_time=1552395875&max_behot_time_tmp=1552395875&tadrequire=true&as=A195BC78877AEBF&cp=5C87AA7E5B9F8E1&_signature=RnjCQwAAGwHsV4LDHvUFkEZ4wl"
#
# "https://www.toutiao.com/api/pc/feed/?category=news_game&utm_source=toutiao&widen=1&max_behot_time=1552395319&max_behot_time_tmp=1552395319&as=A175EC68E78AEEE"

import  requests
from bs4 import BeautifulSoup
import chardet
url = "https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=1552399251&max_behot_time_tmp=1552399251&tadrequire=true&as=A1053C38C7BC30A&cp=5C879CA3403A1E1&_signature=c81xzQAAL03Z4jFND4nvo3PNcd"

proxies = {"https": "http://127.0.0.1:1080"}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
req = requests.get(url,headers=headers,proxies=proxies).text.encode('ascii').decode('unicode_escape')

print(req)
