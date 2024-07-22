from tkinter import *
from tkinter import messagebox
window = Tk()

def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼 꺼짐")
    else:
        messagebox.showinfo("", "체크버튼 켜짐")

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()