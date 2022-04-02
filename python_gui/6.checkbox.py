from tkinter import *

root = Tk()
root.title("Beobsung GUI")
root.geometry("640x480")

chkvar = IntVar()  # chkvar에 int형으로 저장한다.
chkbox = Checkbutton(root, text="오늘하루 보지 않기", variable=chkvar)
chkbox.select()  # 디폴트로 체크박스 체크상태 두기
chkbox.deselect()  # 디폴트로 체크박스 체크상태 해제상태로 두기
chkbox.pack()

chkvar2 = IntVar()  # chkvar2에 int형으로 저장한다.
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기" ,variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())  # 체크상태 출력하기
    print(chkvar2.get())  # 체크상태 출력하기
    # 0 : 체크해제 1 : 체크된상태를 출력

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
