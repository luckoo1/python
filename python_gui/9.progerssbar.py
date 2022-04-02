import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Beobsung GUI")
root.geometry("640x480")

#1
# indeterminate는 결정되지 않음 ,determinate는 그냥 쭈욱 찬다
progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar.start(10)  # 10ms마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop()  # 작동 중지


btn = Button(root, text="중지", command=btncmd)
btn.pack()

#2
p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable = p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) #0.01초 대기
        p_var2.set(i) #progress bar의 값 설정
        progressbar2.update() #for문 동작마다 ui를 update
        print(p_var2.get())

btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop()