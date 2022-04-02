#텍스트는 여러줄 받는 것, 엔트리는 한줄만 받는 것
from tkinter import *

root = Tk()
root.title("Beobsung GUI")
root.geometry("640x480")

txt = Text(root,width=30,height =5) #비어있는 텍스트 위젯만들기
txt.pack()
txt.insert(END,"글자를 입력하세요")#텍스트에 미리 글자 넣어놓기

e = Entry(root,width=30) #여기서는 엔터입력불가 한줄입력만 받음
e.pack()
e.insert(0,"한줄만 입력하세요")#엔트리에 미리 글자 넣어놓기

#버튼을 통해서 텍스트값 가져오기
def btncmd():
    print(txt.get("1.0",END)) #처음부터 END까지있는 모든 텍스트내용을 가져와라
    #1은 line1부터 가져와라.
    #0은 칼럼기준 0번째 위치부터 가져와라

btn1 = Button(root,text = "클릭",command=btncmd)
btn1.pack()

#버튼을 통해서 엔트리값 가져오기
def btncmd():
    print(e.get()) #처음부터 END까지있는 모든 엔트리 내용을 가져와라

btn2 = Button(root,text = "클릭",command=btncmd)
btn2.pack()

#버튼을 통해서 텍스값과 엔트리값 가져온뒤 지우기
def btncmd():
    print(txt.get("1.0",END))#내용출력
    print(e.get())#내용출력
    txt.delete("1.0",END)#내용삭제
    e.delete(0,END)#내용삭제

btn3 = Button(root,text = "클릭",command=btncmd)
btn3.pack()

root.mainloop()