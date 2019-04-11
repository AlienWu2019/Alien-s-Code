# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'turlingApi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from turlingAPI.turling_gui_content import get_content as gc


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(655, 454)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(30, 30, 141, 16))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(170, 20, 221, 30))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Frame)
        self.textBrowser.setGeometry(QtCore.QRect(30, 70, 361, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(440, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 20, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Frame)
        self.pushButton.clicked.connect(self.btn_click)
        self.pushButton_2.clicked.connect(self.btn_clear)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "TurlingApi"))
        self.label.setText(_translate("Frame", "输入要对话的内容:"))
        self.pushButton.setText(_translate("Frame", "确认"))
        self.pushButton_2.setText(_translate("Frame", "清空"))


    def btn_click(self):
        key=self.textEdit.toPlainText()
        self.textBrowser.insertPlainText("我对它说:"+key)
        self.textBrowser.insertPlainText('\n')
        self.textBrowser.insertPlainText("它的回答是:"+gc(key))
        self.textBrowser.insertPlainText('\n')

    def btn_clear(self):
        self.textEdit.clear()
        self.textBrowser.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Frame()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

