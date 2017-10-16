import socket
import threading

host = ''
port = 64932


def Main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(5)
    print "Server start..."
    while True:
        c, addr = s.accept()
        print "connected"
        buf = c.recv(1024)
        writeIn = open("Settings.txt", "w")
        writeIn.write(buf)
        writeIn.close()
        print buf
        print "Fertig"



