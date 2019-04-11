# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import requests
import json

class Ui_Dialog(object):

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

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(613, 277)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(70, 30, 361, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(70, 70, 491, 171))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.btn_click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "英汉翻译"))
        self.pushButton.setText(_translate("Dialog", "翻译"))

    def btn_click(self):
        keyword = self.textEdit.text()
        content = self.result(keyword)
        self.textBrowser.insertPlainText(content)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())