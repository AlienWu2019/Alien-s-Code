from PyQt5.QtCore import QDateTime,Qt

datetime = QDateTime.currentDateTime()

print("Local Date And Time Is:"+datetime.toString(Qt.DefaultLocaleLongDate))
print("Universal Date And Time Is:"+datetime.toUTC().toString())

print("The offset From UTC Is {0}:Seconds".format(datetime.offsetFromUtc()))