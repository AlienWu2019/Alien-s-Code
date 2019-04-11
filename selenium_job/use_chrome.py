from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
open_br = webdriver.Chrome(r'D:\下载安装包文件\chromedriver.exe',options=chrome_options)
open_br.get("https://www.baidu.com")
print(open_br.page_source)
open_br.close()