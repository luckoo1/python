import time
import pyautogui

time_list = [
755	,
1256,
1075,
681,
1071,
892	
]
time.sleep(10)
for i in time_list:
    time.sleep(i)
    time.sleep(6)
    pyautogui.click(x=1766,y=1041)
    time.sleep(5)
    pyautogui.hotkey('space')

time.sleep(5)
pyautogui.click(x=1822,y=133)