import pyqrcode
import png
import socket

class qrcode(object):

    def getqr(self):

        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)
        code = pyqrcode.create(str(IP))
        code.png('ipqr.png', scale=5)