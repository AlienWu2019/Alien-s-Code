# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(60, 150, 251, 87))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Frame)
        self.textEdit_2.setGeometry(QtCore.QRect(50, 70, 104, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Frame)
        self.pushButton.clicked.connect(self.btn_click)
        self.textEdit_2.windowIconTextChanged['QString'].connect(self.pushButton.click)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton.setText(_translate("Frame", "PushButton"))


    def btn_click(self):
        data = self.textEdit_2.toPlainText()
        self.textEdit.insertPlainText(data)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Frame()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())