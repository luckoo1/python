from tkinter import *

root = Tk()
root.title("Beobsung GUI")
root.geometry("640x480")
# =============================================
# btn1 = Button(root,text="버튼1")
# btn2 = Button(root,text="버튼1")

# 그동안 아래처럼 pack()을 활용
# btn1.pack(side = "left")
# btn2.pack(side = "right")

# btn1.grid(row=0,column=0)
# btn1.grid(row=1,column=1)
# =============================================

# 2.Button에 "padx=10,pady=10"를 활용해서 버튼의 크기를 늘림
# 4. pad대신 button에 width=5,height=2쓰면 조절이 가능
btn_f16 = Button(root,text = "F16",width=5,height=2)
btn_f17 = Button(root,text = "F17",width=5,height=2)
btn_f18 = Button(root,text = "F18",width=5,height=2)
btn_f19 = Button(root,text = "F19",width=5,height=2)

# 1. "sticky=N+E+W+S"해서 동서남북 다 늘리기
# 3. grid에 "padx=3,pady=3"넣어서 버튼간 간격을 늘림
#    pad는 글자를 기준으로 간격을 조절한다. 글자수가 다르면 버튼의 크기가 달라질수 있다.

btn_f16.grid(row=0,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_f17.grid(row=0,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_f18.grid(row=0,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_f19.grid(row=0,column=3,sticky=N+E+W+S,padx=3,pady=3)

btn_clear = Button(root,text = "clear",padx=10,pady=10)
btn_equal = Button(root,text = "=",padx=10,pady=10)
btn_div = Button(root,text = "/",padx=10,pady=10)
btn_mul = Button(root,text = "*",padx=10,pady=10)

btn_clear.grid(row=1,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_equal.grid(row=1,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_div.grid(row=1,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_mul.grid(row=1,column=3,sticky=N+E+W+S,padx=3,pady=3)

btn_7 = Button(root,text = "7",padx=10,pady=10)
btn_8 = Button(root,text = "8",padx=10,pady=10)
btn_9 = Button(root,text = "9",padx=10,pady=10)
btn_sub = Button(root,text = "-",padx=10,pady=10)

btn_7.grid(row=2,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_8.grid(row=2,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_9.grid(row=2,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_sub.grid(row=2,column=3,sticky=N+E+W+S,padx=3,pady=3)

btn_4 = Button(root,text = "4",padx=10,pady=10)
btn_5 = Button(root,text = "5",padx=10,pady=10)
btn_6 = Button(root,text = "6",padx=10,pady=10)
btn_plus = Button(root,text = "+",padx=10,pady=10)

btn_4.grid(row=3,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_5.grid(row=3,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_6.grid(row=3,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_plus.grid(row=3,column=3,sticky=N+E+W+S,padx=3,pady=3)

btn_1 = Button(root,text = "1",padx=10,pady=10)
btn_2 = Button(root,text = "2",padx=10,pady=10)
btn_3 = Button(root,text = "3",padx=10,pady=10)
btn_enter = Button(root,text = "enter",padx=10,pady=10)

btn_1.grid(row=4,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_2.grid(row=4,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_3.grid(row=4,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_enter.grid(row=4,column=3,rowspan=2,sticky=N+E+W+S,padx=3,pady=3)

btn_0 = Button(root,text = "0",padx=10,pady=10)
btn_dot = Button(root,text = ".",padx=10,pady=10)

btn_0.grid(row=5,column=0,columnspan=2,sticky=N+E+W+S,padx=3,pady=3)
btn_dot.grid(row=5,column=2,sticky=N+E+W+S,padx=3,pady=3)

root.mainloop()