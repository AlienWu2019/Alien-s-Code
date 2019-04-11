import requests
import re


def get_content(info):
    appkey = "e5ccc9c7c8834ec3b08940e290ff1559"
    url = "http://www.tuling123.com/openapi/api?key=%s&info=%s" % (appkey, info)
    search_str = '{"code":.*?,"text":"(.*?)"}'
    req = requests.get(url).text
    content = req
    search_content = re.compile(search_str)
    result_news = search_content.findall(content)
    str_result_news = "".join(result_news)
    return str_result_news

