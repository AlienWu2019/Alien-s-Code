import tkinter

red = (0,0,255)
root = tkinter.Tk()
root.title('Hello')
root.geometry('400x300')

label1 = tkinter.Label(root,text = 'HelloWorld',bg = red,width = 10,heigth = 2)
label1.pack(side = tkinter.TOP)

root.mainloop()
