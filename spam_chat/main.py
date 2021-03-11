import pyautogui
import time
import datetime


time.sleep(5)

for i in range(100):
    x = datetime.datetime.now()
    pyautogui.typewrite(x)
    pyautogui.press("enter")
    time.sleep(1)