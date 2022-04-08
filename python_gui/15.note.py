import os
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

# 열기, 저장파일 이름
filename = "mynote.txt"

def open_file():
	if os.path.isfile(filename): #file있으면 ture 없으면 false
		with open(filename,"r",encoding="uft8") as file:
			txt.delete("1.0",END) #텍스트 위젯 본문 삭제
			txt.insert(END,file.read())#파일 내용을 본문에 입력

def save_file():
	with open(filename,"r",encoding="uft8") as file:
		file.write(txt.get("1.0",END)) #모든 내용을 가져와서 저장

menu = Menu(root)

menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label="열기",command = open_file)
menu_file.add_command(label="저장",command = save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기",command=root.quit)

menu.add_cascade(label="파일",menu=menu_file)
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")
root.config(menu=menu)

#스코롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y") #fill에 y를 줘서 위아래로 스크롤 이동

#본문영역
txt =Text(root,yscrollcommand=scrollbar.set) #스크롤바와 txt매핑
txt.pack(side="left",fill="both",expand=True) #전체공간 꽉 채우기
scrollbar.config(command = txt) #스크롤바와 txt매핑
root.mainloop()