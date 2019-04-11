from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class My_Project(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "My_Project"
        self.top = 100
        self.left = 100
        self.width = 680
        self.heigh = 500
        self.setWindowIcon(QtGui.QIcon("material01.png"))
        self.InitWindow()


    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.heigh)
        self.show()

App = QApplication(sys.argv)
window = My_Project()
sys.exit(App.exec())

