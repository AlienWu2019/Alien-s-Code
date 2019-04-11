# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baike.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import requests
from pyquery import PyQuery as pq
import re


class Baike_baidu:
    def __init__(self,key):
        url1="https://baike.baidu.com/item/"
        self.url = url1+key

    #获取网页的html
    def html(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
        req=requests.get(self.url,headers=headers)
        html=req.content
        html_doc=str(html,'utf-8')
        return html_doc

    #抓取百度百科概述
    def search_news_Summary(self):
        content=pq(self.html())
        result=content(".lemma-summary .para").text()
        result2 = result.replace('\xa0','')
        result3 = result2.replace(' ', '')
        return result3

    #抓取表格字条
    def search_news_form(self):
        content=pq(self.html())
        result1=content('.basic-info')
        result2=result1('.basicInfo-block').text()
        result3 = result2.replace('\n',':')
        result4 = result3.replace('\xa0','')
        return result4

    #抓取标题名称
    def search_news_title(self):
        search_news_str='<h2 class="title-text"><span class="title-prefix">.*?</span>(.*?)</h2>'
        content = pq(self.html())
        title1 = content('.para-title')
        title2 = title1('.title-text')
        str_title2 = str(title2)
        search = re.compile(search_news_str)
        result = search.findall(str_title2)
        return result

    #抓取内容:
    def search_news_content(self):
        search_news_str = '<div class="para" label-module="para">(.*)</div>'
        search_news_str1 = '<[^>]*>'
        content = pq(self.html())
        search = re.compile(search_news_str)
        str_content = str(content)
        result = search.findall(str_content)
        result_clear = result.remove(result[0])
        result_str = "".join(result)
        search2 = re.compile(search_news_str1)
        result_str2 = search2.sub('',result_str)
        return result_str2

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
        self.pushButton.setGeometry(QtCore.QRect(550, 10, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(680, 10, 93, 41))
        self.pushButton2.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 400, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.btn_click)
        self.pushButton2.clicked.connect(self.btn_clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "百度百科"))
        self.label.setText(_translate("Dialog", "输入关键字："))
        self.groupBox.setTitle(_translate("Dialog", "Content"))
        self.groupBox_2.setTitle(_translate("Dialog", "Form"))
        self.groupBox_3.setTitle(_translate("Dialog", "Summary"))
        self.pushButton.setText(_translate("Dialog", "search"))
        self.pushButton2.setText(_translate("Dialog", "clear"))

    def btn_click(self):
        key=self.lineEdit.text()
        summary=Baike_baidu(key).search_news_Summary()
        form=Baike_baidu(key).search_news_form()
        content=Baike_baidu(key).search_news_content()
        self.textBrowser.insertPlainText(summary)
        self.textBrowser_2.insertPlainText(form)
        self.textBrowser_3.insertPlainText(content)

    def btn_clear(self):
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.textBrowser_3.clear()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())