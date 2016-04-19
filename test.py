import win32api, win32con
import time

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,480,540)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,480,540)

time.sleep(2)


count = 100000

j = 0
for i in range(count):
    leftClick()
    w = int(i/count * 100)
    if w != j:
        print(w,"%")
        j = w