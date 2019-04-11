import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

#0,导入数据集
basestation ="D://test/first.xlsx"
df = pd.read_excel(basestation,'Sheet1')

#1,直方图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(df['Age'],bins=7)
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('Employee')
plt.show()
