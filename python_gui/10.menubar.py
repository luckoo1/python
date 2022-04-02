from tkinter import *

root = Tk()
root.title("Beobsung GUI")
root.geometry("640x480")

def create_new_file():
    print("새 파일을 만듭니다.")

#file레이블 추가
menubar = Menu(root) #1.root에 menubar를 만들었었다

menu_file = Menu(menubar,tearoff= 0) #3."file_menu"를 만들건데 menubar를 넣자
menu_file.add_command(label = "New File", command = create_new_file)
menu_file.add_command(label = "New Window")
menu_file.add_separator() #구분자 추가
menu_file.add_command(label="Open file")
menu_file.add_separator() #구분자 추가
menu_file.add_command(label="Save all",state = "disable") #disable은 menubar가 비활성화
menu_file.add_separator() #구분자 추가
menu_file.add_command(label="Exit",command = root.quit) #Exit누르면 화면이 꺼진다.

menubar.add_cascade(label = "File",menu=menu_file) #4.지금까지 만든 menu_bar를 File이라는 레이블에 추가함

#Edit 레이블(빈 값)
menubar.add_cascade(label = "Edit") #5.Edit레이블만 추가함

# Language레이블 추가(radio button)
menu_lang = Menu(menubar,tearoff = 0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menubar.add_cascade(label = "Language",menu = menu_lang) #6.Language 레이블을 만들어서 menu_lang을 추가

# view lable추가(check box)
menu_view = Menu(menubar, tearoff =0)
menu_view.add_checkbutton(label = "Show Minimap")
menubar.add_cascade(label = "View", menu = menu_view) #7.view 레이블을 만들어서 menu_view를 추가

root.config(menu = menubar) #2.root의 config에 menubar를 넣음
root.mainloop()