# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import re
from pyquery import PyQuery as pq
from Pyquery的应用.百度百科API.baike_baidu import Baike_baidu as bk

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(790, 607)
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(80, 40, 411, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(550, 40, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Frame)
        self.textBrowser.setGeometry(QtCore.QRect(80, 120, 651, 421))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Frame)
        self.textEdit.windowIconTextChanged['QString'].connect(self.pushButton.click)
        self.pushButton.clicked.connect(self.btn_click)
        QtCore.QMetaObject.connectSlotsByName(Frame)


    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton.setText(_translate("Frame", "PushButton"))


    def btn_click(self):
        key=self.textEdit.toPlainText()
        a=bk(key).search_news_Summary()

        self.textBrowser.insertPlainText(a)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Frame()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())