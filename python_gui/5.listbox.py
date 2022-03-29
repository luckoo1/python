#list box는 여러줄에 걸쳐서 관리하는 위젯
from tkinter import *

root = Tk()
root.title("Beobsung GUI")
root.geometry("640x480+300+100")


listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "바나나")
listbox.insert(2, "딸기")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

# selectmode가 "single"이면 하나만 선택가능, "extended"는 여러개 선택가능
# height가 0이면 모든거 다 보여주는데 3이라고 적으면 3개만 보여줌(키보드로 내리면 다 볼수있긴하다)


def btncmd1():
    listbox.delete(END)  # 리스트박스 맨뒤에것 삭제
    listbox.delete(0)  # 리스트박스 맨앞에것 삭제

def btncmd2():
    print("리스트에는", listbox.size(), "개")  # 리스트박스 사이즈 출력


def btncmd3():
    print("1~3번째 항목은", listbox.get(0, 2))  # 리스트박스 인덱스 맞게 출력


def btncmd4():
    print("선택된항목", listbox.curselection())  # 선택된 항목 확인이 인덱스값으로 반환


btn1 = Button(root, text="클릭", command=btncmd1)
btn1.pack()


btn2 = Button(root, text="클릭", command=btncmd2)
btn2.pack()

btn3 = Button(root, text="클릭", command=btncmd3)
btn3.pack()

btn4 = Button(root, text="클릭", command=btncmd4)
btn4.pack()

root.mainloop()