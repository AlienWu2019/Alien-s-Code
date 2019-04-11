import xlsxwriter

#创建一个工作薄并添加一张工作表，当然工作表是可以命名的
workbook = xlsxwriter.Workbook('Expenses02.xlsx')
worksheet = workbook.add_worksheet('Data')

#添加用于突出显示单元格的粗体格式。
bold = workbook.add_format({'bold':True})

#为显式钱的单元格添加数字格式
money = workbook.add_format({'num_format': '$#,##0'})

#写一些标题
worksheet.write('A1','Item',bold)
worksheet.write('B1','Cost',bold)


#下面是我们要插入的数据
expenses = (
    ['Rent',1000],
    ['Gas',  100],
    ['Food', 300],
    ['Gym',   50],
)

#从第一个单元格开始，行和列的索引均为0
row = 1
col = 0

#迭代数据并逐行写入
for item,cost in (expenses):
    worksheet.write(row,col,   item)
    worksheet.write(row,col+1,cost,money)
    row+=1

#写一个公式，计算出总和
worksheet.write(row,0,'Total',bold)
worksheet.write(row,1,'=SUM(B2:B5)',money)

workbook.close()
