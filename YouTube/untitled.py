# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(601, 124)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 10, 331, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(130, 60, 331, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(490, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 60, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.lineEdit.windowIconTextChanged['QString'].connect(self.pushButton.click)
        self.pushButton.clicked.connect(Form.show)
        self.pushButton_2.clicked.connect(self.lineEdit.show)
        self.pushButton_2.clicked.connect(self.textBrowser.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "输入视频url："))
        self.label_2.setText(_translate("Form", "状态："))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "清空"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())