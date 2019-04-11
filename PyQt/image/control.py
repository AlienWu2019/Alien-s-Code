from PyQt.image.test2 import Ui_Frame
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
import sys

class myWindow(QWidget,Ui_Frame):
    def __init__(self):
        super(myWindow,self).__init__()
        self.setupUi(self)

    def btn_click(self):
        self.textEdit.insertPlainText('helloword')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w=myWindow()
    w.pushButton.click.connect(w.btn_click)
    w.show()
    sys.exit(app.exec_())
