import demo
import wx


class CalcFrame(demo.MyFrame1):
    def __init__(self,parent):
        demo.MyFrame1.__init__(self,parent)

    def mySquare( self, event ):
        num = int(self.m_textCtrl3.GetValue())
        self.m_textCtrl4.SetValue(str(num*num))

app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)

app.MainLoop()

