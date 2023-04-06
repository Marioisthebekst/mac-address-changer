import subprocess
from tkinter import *

WIN = Tk()
WIN.geometry("500x300")
WIN.title("Mac Adress Changer")

def changing_the_address():
    subprocess.call("ifconfig eth0 down", shell=True)
    subprocess.call(f'ifconfig eth0 hw ether {text.get()}',shell=True)
    subprocess.call("ifconfig eth0 up",shell=True)

    subprocess.call("ifconfig",shell= True)

lbl = Label(WIN, text="type your new mac address, example- 22:11:22:33:44:55")
lbl.pack()
lbl = Label(WIN, text="note the address works only for eth0***")
lbl.pack()
text = Entry(WIN)
text.pack()

btn = Button(WIN, text="Confirm", bg="#cce3e6", fg="black", command= changing_the_address)
btn.pack()

WIN.mainloop()
