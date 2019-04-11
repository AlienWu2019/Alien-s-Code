import xlsxwriter

#创建一个工作薄并添加一张工作表，当然工作表是可以命名的
workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet('Data')

#下面是我们要插入的数据
expenses = (
    ['Rent',1000],
    ['Gas',  100],
    ['Food', 300],
    ['Gym',   50],
)

#从第一个单元格开始，行和列的索引均为0
row = 0
col = 0

#迭代数据并逐行写入
for item,cost in (expenses):
    worksheet.write(row,col,   item)
    worksheet.write(row,col+1,cost)
    row+=1

#写一个公式，计算出总和
worksheet.write(row,0,'Total')
worksheet.write(row,1,'=SUM(B1:B4)')

workbook.close()
