# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import re
from pyquery import PyQuery as pq

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(801, 574)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 360, 781, 211))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 21, 761, 181))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 200, 781, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 20, 761, 131))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 60, 781, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 761, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(650, 10, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 521, 41))
        self.lineEdit.setObjectName("lineEdit")



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "百度百科"))
        self.label.setText(_translate("Dialog", "输入关键字："))
        self.groupBox.setTitle(_translate("Dialog", "Content"))
        self.groupBox_2.setTitle(_translate("Dialog", "Form"))
        self.groupBox_3.setTitle(_translate("Dialog", "Summary"))
        self.pushButton.setText(_translate("Dialog", "search"))

     #获取url
    def get_url(self,key):
        url1 = "https://baike.baidu.com/item/"
        self.url = url1 + key

    #获取html
    def get_html(self):
        hearders = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
        req = requests.get(self.url,hearders=hearders)
        html = req.content
        html_real = str(html,'utf-8')
        self.html = html_real

    # 抓取百度百科概述
    def get_summary(self):
        html_pq = pq(self.html)
        content = html_pq(".lemma-summary .para").text()
        content1 = content.replace('\xa0','')
        result = content1.replace(' ', '')
        return result

    #抓取form
    def get_form(self):
        content = pq(self.html)
        result1 = content('.basic-info')
        result2 = result1('.basicInfo-block').text()
        result3 = result2.replace('\n', ':')
        result4 = result3.replace('\xa0', '')
        return result4

    #抓取主要内容
    def get_content(self):
        search_news_str = '<div class="para" label-module="para">(.*)</div>'
        search_news_str1 = '<[^>]*>'
        content = pq(self.html)
        search = re.compile(search_news_str)
        str_content = str(content)
        result = search.findall(str_content)
        result_clear = result.remove(result[0])
        result_str = "".join(result)
        search2 = re.compile(search_news_str1)
        result_str2 = search2.sub('', result_str)
        return result_str2

    #点击search事件
    def button_click(self):
        key = self.lineEdit.text()  #获取文本的内容作为关键字
        url = self.get_url(key)
        self.textBrowser.print(self.get_summary())
        self.textBrowser_2.print(self.get_form())









#实例化
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.button_click()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

