import jisuanqi
import wx

class jisuan(jisuanqi.MyFrame1):
    def __init__(self,parent):
        jisuanqi.MyFrame1.__init__(self,parent)
        #按钮常值
    def e1(self,event):
        num0 = self.m_button13.LabelText
        self.m_textCtrl1.SetValue(num0)
        x0 = int (num0)
        return x0

    def e5( self, event ):
        num1 = self.m_button9.LabelText
        self.m_textCtrl1.SetValue(num1)
        x1 = int (num1)
        return x1

    def e6( self , evnet ):
        num2 = self.m_button10.LabelText
        self.m_textCtrl1.SetValue(num2)
        x2 = int (num2)
        return x2

    def e7( self, event ):
        num3 = self.m_button11.LabelText
        self.m_textCtrl1.SetValue(num3)
        x3 = int (num3)
        return x3

    def e9( self, event ):
        num4 = self.m_button5.LabelText
        self.m_textCtrl1.SetValue(num4)
        x4 = int (num4)
        return x4

    def e10( self, event ):
        num5 = self.m_button6.LabelText
        self.m_textCtrl1.SetValue(num5)
        x5 = int (num5)
        return x5

    def e11( self, event ):
        num6 = self.m_button7.LabelText
        self.m_textCtrl1.SetValue(num6)
        x6 = int (num6)
        return x6

    def e13( self, event ):
        num7 = self.m_button1.LabelText
        self.m_textCtrl1.SetValue(num7)
        x7 = int (num7)
        return x7

    def e14( self, event ):
        num8 = self.m_button2.LabelText
        self.m_textCtrl1.SetValue(num8)
        x8 = int (num8)
        return x8

    def e15( self, event ):
        num9 = self.m_button3.LabelText
        self.m_textCtrl1.SetValue(num9)
        x9 =int (num9)
        return x9

    #处理事件/
    def e16( self, event ):
        str1 = self.m_button4.GetLabelText()
        self.m_textCtrl1.SetValue(str1)

    #处理事件*
    def e12( self, event ):
        pass

    #处理事件-
    def e8( self, event ):
        pass

    #处理事件+
    def e4( self, event ):
        pass






    #待实现
app = wx.App(False)
frame = jisuan(None)
frame.Show(True)

app.MainLoop()
