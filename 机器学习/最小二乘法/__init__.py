##最小二乘法
import numpy as np #科学计算库
import scipy as sp #在numpy基础上实现的部分算法库
import matplotlib.pyplot as plt #会图库
import matplotlib
from scipy.optimize import leastsq #引入最小二乘法算法

"""
   设置样本数据，真实数据需要在这里处理
"""
#样本数据(Xi,Yi),需转换成数组(列表)形式
Xi = np.array([6.19,2.51,7.29,7.01,5.7,2.66,3.98,2.5,9.1,4.2])
Yi = np.array([5.25,2.83,6.41,6.71,5.1,4.23,5.05,1.98,10.5,6.3])
print(Xi)
print(Yi)

'''
  设定拟合函数和偏差函数
  函数的性转确定过程：
  1，先画样本图像
  2，根据样本图像打支形状确定函数形式（直线，抛物线，正弦余弦等）
'''

##需要拟合的函数func：指定函数的形状 p是一个元祖(k,b)
def func(p,x):
    k,b = p
    return k*x+b

##偏差函数：x.y都是列表：这里的x,y跟上面的Xi，Yi中是一一对应的
def error(p,x,y):
    return func(p,x)-y

#k,b的初始值，可以任意设定，经过几次试验，发现p0的值会影响cost的值：Para[1]
p0 = [1,20]

#发error函数中出了p0意外的参数打包到args中
Para = leastsq(error,p0,args=(Xi,Yi))

#读取结果
k,b = Para[0]
print("k=",k," b=",b)
print("cost=",Para[1])
print("y="+str(round(k,2))+"x+"+str(round(b,2))) #拟合直线

#画样本点
plt.figure(figsize=(8,6))  #指定图像比例：8：6
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码问题
plt.scatter(Xi,Yi,color="green",label="样本数据",linewidth=2)

#画拟合直线
x = np.linspace(0,12,100)  #在0-12直接画100个连续点
y=k*x+b ##函数式
plt.rcParams['font.sans-serif']=['SimHei']
plt.plot(x,y,color="red",label="拟合直线",linewidth=2)
plt.legend(loc='lower right') #绘制图例
plt.show()