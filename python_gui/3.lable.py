from tkinter import *

root = Tk()
root.title("Beobsung GUI")

lable1 = Label(root,text = "Hello")
lable1.pack()

photo = PhotoImage(file = "python_gui/img.png")
lable2 = Label(root,image = photo)
lable2.pack()



root.mainloop()