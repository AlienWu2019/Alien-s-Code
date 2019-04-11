from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    # *args接受元组类参数
    # **kwargs接受字典类参数
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.windowTitleChanged.connect(lambda x:self._my_func('shiyanlou',666))

        #设置窗口标题
        self.setWindowTitle('My First App')

        #设置标签
        label=QLabel('Welcome to Shiyanlou!')

        #设置标签显示在中央
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    def _my_func(self,s='my_func',a=100):
        dic = {'s':s,'a':a}


#创建应用实例，通过sys.argv传入命令行参数
app=QApplication(sys.argv)
#创建窗口实例
window=MainWindow()
#显示窗口
window.show()
#只想应用，进入事件循环
app.exec_()





