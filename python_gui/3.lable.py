from tkinter import *

root = Tk()
root.title("Beobsung GUI")

#lable은 글자나 이미지만 보여준다

lable1 = Label(root,text = "Hello")
lable1.pack()

photo = PhotoImage(file = "python_gui/img1.png")
lable2 = Label(root,image = photo)
lable2.pack()

#버튼눌렀을때 프로그램 실행상에서 바꿔보기
def change():
    lable1.config(text = "Bye")
    global photo2 #전역변수로 해줘야지 함수에서 나가도 유지된다(garbage collection때문에)
    photo2 = PhotoImage(file = "python_gui/img2.png")
    lable2.config(image = photo2)

btn = Button(root,text="Click",command=change)
btn.pack()

root.mainloop()