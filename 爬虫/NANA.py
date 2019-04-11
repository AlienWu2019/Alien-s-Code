import requests
from bs4 import BeautifulSoup
import xlsxwriter

workbook = xlsxwriter.Workbook('NANA茶楼话题历史.xlsx')
worksheet = workbook.add_worksheet('Data')
data_list=[]
row = 0
col = 0

for i in range(1,1000):
    url="http://nanabt.com/index.php?c=thread&fid=28&page={0}".format(i)
    req=requests.get(url=url)
    html=req.text
    bs = BeautifulSoup(html)
    texts = bs.find_all('p',class_='title')
    for i in range(2,25):
        fp=texts[i].text
        data_list.append(fp)
    for data in data_list:
        worksheet.write(row,col,data)
        row+=1
workbook.close()



