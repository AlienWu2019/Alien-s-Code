import numpy as np
import matplotlib as plt

def mandebrot(h,w,maxit=20):
    y,x = np.ogrid[-1.4:1.4:h*1j,-2:0.8:w*1j] #复数步长的设置是通过j进行设置的，如5j。复数前表示的是，用几个数值来等分整个区间,等差数列
