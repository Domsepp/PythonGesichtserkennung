from Tkinter import *
from PIL import Image, ImageTk
from QR import qrcode
from PaulsGesicht import run

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"


    def createWidgets(self):
        qropen.getqr()
        image = Image.open('ipqr.png')
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.image = photo
        label.pack()

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack()

        self.hi_there = Button(self)
        self.hi_there["text"] = "Start Program",
        self.hi_there["command"] = run()

        self.hi_there.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        run()

qropen = qrcode()
root = Tk()
app = Application(master=root)
app.mainloop()