from tkinter import *
root = Tk()

computerLanguages = ['C','C++','Python','Java']
huamLanguage = ['Chinese','English','Spanish']
listbox1 = Listbox(root)
listbox2 = Listbox(root)
for item in computerLanguages:
    listbox1.insert(0,item)
for item in huamLanguage:
    listbox2.insert(0,item)

listbox1.pack()
listbox2.pack()
root.mainloop()