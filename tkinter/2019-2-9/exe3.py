from tkinter import *

def clickButton():
    print('hello button')

root = Tk()
Button(root,text='MyButton',command=clickButton).pack()
root.mainloop()