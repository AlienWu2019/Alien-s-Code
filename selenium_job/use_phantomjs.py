from selenium import webdriver

browser = webdriver.PhantomJS(r'D:\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
browser.get("https://www.baidu.com")
print(browser.page_source)