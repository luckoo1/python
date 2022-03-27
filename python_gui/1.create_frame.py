from tkinter import *

#창에 관한것
root = Tk()
root.title("Beobsung GUI") #파일이름
root.geometry("640x480+300+100") #(가로크기*세로크기)+(x좌표+y좌표)에 뜬다
root.resizable(False,False) #x(너비), y(높이) 값 변경 불가 (창크기 변경 불가)

root.mainloop() #계속 실행을 위한것