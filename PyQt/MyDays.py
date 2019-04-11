from PyQt5.QtCore import QDateTime,Qt

datetime = QDateTime.currentDateTime()


print("Today Date And Time Is:"+datetime.toString(Qt.ISODate))
print("Adding 12 Days To The Date: {0}".format(datetime.addDays(12).toString(Qt.ISODate)))
print("Subtracting 25 Days:{0}".format(datetime.addDays(-25).toString(Qt.ISODate)))
print("Adding 50 Seconds:{0}".format(datetime.addSecs(50).toString(Qt.ISODate)))
print("Adding 3 Months: {0}".format(datetime.addMonths(3).toString(Qt.ISODate)))