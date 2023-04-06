import subprocess
from tkinter import *

WIN = Tk()
WIN.geometry("500x300")
WIN.title("Mac Adress Changer")

lbl = Label(WIN, text="type your new mac address, example- 11:22:33:44:55:66")
lbl.pack()
text = Entry(WIN)
text.pack()


WIN.mainloop()
