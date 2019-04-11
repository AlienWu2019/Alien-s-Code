import win32api
import win32con
import time

def windows_action():

    """
    1.打开程序事件
    """
    #鼠标移动到图标位置
    win32api.SetCursorPos((346, 55))
    #左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    #左键松开
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    # 左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # 左键松开
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    #此时间事电脑性能而定，若电脑启动QQ慢的话就设置时间长一些
    time.sleep(3)

    """
    2.输入QQ信息事件
    """
    #移动到头像位置
    win32api.SetCursorPos((775, 383))
    #点击头像
    # 左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # 左键松开
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(0.5)
    #三次Tab时间
    for i in range(3):
        win32api.keybd_event(9, 0, 0, 0)
        win32api.keybd_event(9 , 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)
    """
    输入账号:******** 键盘对应的键码
    """
    win32api.keybd_event(50, 0, 0, 0)
    win32api.keybd_event(50, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(55, 0, 0, 0)
    win32api.keybd_event(55, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(51, 0, 0, 0)
    win32api.keybd_event(51, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(48, 0, 0, 0)
    win32api.keybd_event(48, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(57, 0, 0, 0)
    win32api.keybd_event(57, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(51, 0, 0, 0)
    win32api.keybd_event(51, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(51, 0, 0, 0)
    win32api.keybd_event(51, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(57, 0, 0, 0)
    win32api.keybd_event(57, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(50, 0, 0, 0)
    win32api.keybd_event(50, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(52, 0, 0, 0)
    win32api.keybd_event(52, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)

    """
    输入密码：****** 键盘对应的键码
    """
    #Tab
    win32api.keybd_event(9, 0, 0, 0)
    win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    # 键盘事件
    win32api.keybd_event(81, 0, 0, 0)
    win32api.keybd_event(81, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(81, 0, 0, 0)
    win32api.keybd_event(81, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(56, 0, 0, 0)
    win32api.keybd_event(56, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(56, 0, 0, 0)
    win32api.keybd_event(56, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(50, 0, 0, 0)
    win32api.keybd_event(50, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(50, 0, 0, 0)
    win32api.keybd_event(50, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(55, 0, 0, 0)
    win32api.keybd_event(55, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(50, 0, 0, 0)
    win32api.keybd_event(50, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(54, 0, 0, 0)
    win32api.keybd_event(54, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    win32api.keybd_event(48, 0, 0, 0)
    win32api.keybd_event(48, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)

    time.sleep(0.5)

    """
    3.登录事件
    """
    #登录事件
    # 移动到登录位置
    win32api.SetCursorPos((789, 564))
    # 左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # 左键松开
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


windows_action()