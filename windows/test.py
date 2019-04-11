import win32api
import win32con
import time

def windows_action():
    #鼠标移动到图标位置
    win32api.SetCursorPos((1274, 835))
    #左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    #左键松开
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

    time.sleep(1)

    #鼠标移动到确认位置
    win32api.SetCursorPos((798, 603))
    #左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    #左键松开
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

