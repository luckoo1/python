from tkinter import *

root = Tk()
root.title("Beobsung GUI")

#버튼에 관한것
btn1 = Button(root, text="button1")  # root에 button1을 나타내겠다.
btn1.pack()  # 이걸 적어줘야 포함된다

btn2 = Button(root, padx=5, pady=10, text="button2") #버튼크기 조절, 글자크기에서 x+5 y+10만큼 공간확보(여백정보를 알려주는 것)
btn2.pack()

btn3 = Button(root, padx=5, pady=10, text="button33333333333333") #버튼크기 조절,글자양에따라 버튼크기가 달라짐
btn3.pack()

btn4 = Button(root, width=10, height=5, text="button4")#버튼크기 조절, 그냥 버튼 크기 조절(고정크기)
btn4.pack()

btn5 = Button(root, fg="red",bg="yellow",text="button5")#버튼크기 조절, 그냥 버튼 크기 조절(고정크기)
btn5.pack()

photo = PhotoImage(file="python_gui/img.png")#이미지로 버튼 표현
btn6 = Button(root, image = photo)
btn6.pack()

#버튼동작설정
def btncmd():
    print("button is clicked!")
btn7 = Button(root,text="동작버튼",command = btncmd)
btn7.pack()

root.mainloop()