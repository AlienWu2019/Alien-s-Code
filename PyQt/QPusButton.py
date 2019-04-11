import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QToolTip


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Push Button"
        self.left = 100
        self.top = 100
        self.width = 680
        self.height = 540

        self.setWindowIcon(QtGui.QIcon("material01.png"))
        button = QPushButton("Close",self)
        button.move(270,340)
        button.setToolTip("<h3>This Is Click Button</h3>")
        self.InitGUI()

    def InitGUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
