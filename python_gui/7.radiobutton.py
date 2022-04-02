from tkinter import *

root = Tk()
root.title("Beobsung GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()  # 코드줄 줄이기 위해 이렇게 사용

#Radiobutton은 여러개 button중 하나의 button선택할수 있게 하는 것

burger_var = IntVar()  # 여기에 int형으로 값을 저장
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()  # 디폴트로 btn_burger1선택되있게 함
btn_burger2 = Radiobutton(root, text="치즈햄버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨햄버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()  # 코드줄 줄이기 위해 이렇게 사
drink_var = StringVar()  # 여기에 string형으로 값을 저장
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="환타", value="환타", variable=drink_var)
btn_drink3 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get())  # 선택된 라디오 항목의 값(value) 반환
    print(drink_var.get())  


btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()