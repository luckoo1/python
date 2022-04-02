import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Beobsung GUI")
root.geometry("640x480")
# 1
values = [str(i)+"일" for i in range(1, 32)]  # 1~32까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values) #heigt는 화살표 눌렀을때 보이는 목록의 수
combobox.pack()
combobox.set("카드 결제일")  # 최초 목록 제목 설정
# 2
#위의 콤보박스는 콤보박에서 글을 적을수있지만 이건 불가능
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) #0번째 인덱스 값이 디폴트로 설정
readonly_combobox.pack()

def btncmd():
    print(combobox.get())  # 선택된 값 표시
    print(readonly_combobox.get())  # 선택된 값 표시

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()