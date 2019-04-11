import tkinter as tk

class Appliication(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there=tk.Button(self)
        self.hi_there["text"]="Hello World\n(click me)"
        self.hi_there["command"]=self.say_hi
        self.hi_there.pack(side="top")

        self.quit=tk.Button(self,text="QUIT",fg="red")
        self.quit["command"] = self.say_bye
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there,everyone")

    def say_bye(self):
        print("goodbye!")
        root.destroy()

root=tk.Tk()
app=Appliication(master=root)
app.mainloop()