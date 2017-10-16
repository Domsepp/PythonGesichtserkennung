from Tkinter import *
from PIL import Image, ImageTk
from QR import qrcode
from Gesicht import run
from SettingSaver import Main
from thread import start_new_thread
import time

def start():
    run()
def connect():
    start_new_thread(Main,())

qropen = qrcode()


b=Button(text="Start", command = start)
b.pack()
c=Button(text="Connect to App", command=connect)
c.pack()
qropen.getqr()
image = Image.open('ipqr.png')
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image = photo
label.pack()

mainloop()
