from wx import *
import  wx


app = wx.App()
window = wx.Frame(None,title = 'Helloworld',size = (300,200))
panel = wx.Panel(window)
label = wx.StaticText(panel,label = 'Helloworld',pos= (100,60))
window.Show(True)
app.MainLoop()



