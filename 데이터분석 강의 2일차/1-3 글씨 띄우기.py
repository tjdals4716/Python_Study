from tkinter import *
window = Tk()

label1 = Label(window, text = "hi there, 안녕하세요")
label2 = Label(window, text = "빈갑습니다", font = ("궁서체 ", 30), fg = "blue")
label3 = Label(window, text = "파이썬 공부중입니다.", bg = "magenta", width = 20, height = 5, anchor = SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()