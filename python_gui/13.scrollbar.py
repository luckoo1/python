from tkinter import *

root = Tk()
root.title("Beobsung GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side = "right",fill ="y")

listbox = Listbox(frame,selectmode="extended",height =10,yscrollcommand=scrollbar.set)
#scrollbar.set이 없으면 scroll이 동작을 안함, 내려도 올라감

for i in range(1,32):
    listbox.insert(END,str(i)+"일")
listbox.pack(side = "left")

scrollbar.config(command=listbox.yview) #이게 있어야 막대바로 control가능

root.mainloop() 