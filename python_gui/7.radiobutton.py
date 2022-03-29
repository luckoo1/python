from tkinter import *

root = Tk()
root.title("Beobsung GUI")
root.geometry("640x480+300+100")

Label(root, text ="메뉴를 선택하세요").pack() #코드줄 줄이기 위해 이렇게 사용

def btncmd():
    pass

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
