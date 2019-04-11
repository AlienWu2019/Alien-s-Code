import requests
import re

def get_ip_by_ip138():
    response = requests.get("http://www.baidu.com")
    ip = re.search(r"\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]",response.content.decode(errors='ignore'))
    return ip

print("本机的ip地址为:",get_ip_by_ip138())