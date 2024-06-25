from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("고양이 버튼", "고양이")

window = Tk()

photo = PhotoImage(file = "/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/GIF/cat7.gif")
button = Button(window, image = photo, command = myFunc)

button.pack()

window.mainloop()