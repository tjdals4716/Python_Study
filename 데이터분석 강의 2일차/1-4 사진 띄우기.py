from tkinter import *
window = Tk()

photo = PhotoImage(file = "/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/GIF/cat7.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()