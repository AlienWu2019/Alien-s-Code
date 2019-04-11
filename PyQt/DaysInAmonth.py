from PyQt5.QtCore import QDate

date = QDate.currentDate()

d = QDate(2011,11,23)
print("2011 Days In A Month:{0}".format(d.daysInMonth()))
print("2011 Days In A Years:{0}".format(d.daysInYear()))

print()
print("now Days In A Month:{0}".format(date.daysInMonth()))
print("now Days In A Years:{0}".format(date.daysInYear()))