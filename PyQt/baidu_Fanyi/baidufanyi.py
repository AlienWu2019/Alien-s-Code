# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baidufanyi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import requests
import json

class Ui_Frame(object):

    def result(self,keyword):
        url = "https://fanyi.baidu.com/extendtrans"
        # 设置提交数据
        posData = {"query": keyword,
                   "from": "en",
                   "to": "zh"}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36'
        }
        req = requests.post(url,posData,headers=headers)
        json_data = json.loads(req.content.decode())

        # 然后我们可以通过格式化工具进行json的解析
        return ','.join(json_data["data"]["st_tag"])

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(642, 300)
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(410, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Frame)
        self.textBrowser.setGeometry(QtCore.QRect(30, 80, 581, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 20, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Frame)
        self.pushButton.clicked.connect(self.btn_click)
        self.lineEdit.windowIconTextChanged['QString'].connect(self.pushButton.click)
        self.pushButton_2.clicked.connect(self.btn_clear)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "英汉翻译"))
        self.pushButton.setText(_translate("Frame", "翻译"))
        self.pushButton_2.setText(_translate("Frame", "清除"))

    def btn_click(self):
        keyword = self.lineEdit.text()
        content = self.result(keyword)
        self.textBrowser.insertPlainText(content)

    def btn_clear(self):
        self.lineEdit.clear()
        self.textBrowser.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Frame()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())


