import requests
import re
import xlsxwriter

workbook = xlsxwriter.Workbook('dgut_OJ系统题库.xlsx')
worksheet = workbook.add_worksheet('Data')
row = 0
col = 0

for i in range(4,1151):
    url="http://oj.dgut.edu.cn/api/xproblem/{0}/".format(i)
    search=r'"title":"(.*?)"'
    font=r'<p>(.*?)</p>'
    req=requests.get(url)
    html=req.text

    content_title=re.compile(search)
    result_title=content_title.findall(html)

    contnet_font=re.compile(font)
    result_font=contnet_font.findall(html)

    title="".join(result_title)
    content="".join(result_font)


    worksheet.write(row,col,title)
    worksheet.write(row+1,col,content)
    row+=2


workbook.close()




