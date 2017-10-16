import numpy as np
import cv2
import sqlite3
from Mail import sendMail
from thread import start_new_thread
from threading import Thread
import time
import urlparse

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
cap = cv2.VideoCapture(0);
rec = cv2.createLBPHFaceRecognizer();
# rec.load("recognizer\\trainningData.yml")

id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,1,.5,0,2,1)

lag = False
test = 0
start = False
timerfinished = True
Mails = 0


def sendMails():
    global start
    global test
    global Mails
    print "[*]Thread Mail start.\n"
    readMails = open("Settings.txt").read()
    print readMails
    readlines = readMails.split(',')
    print readlines
    while Mails < len(readlines):
        if "\n" not in readlines[Mails]:
            #sendMail(readlines[Mails], 'Security Camera', 'Raspberry pi security camera update', 'img2.jpg')
            Mails += 1
        else:
            readlines[Mails] = readlines[Mails].replace("\n", "")
            #sendMail(readlines[Mails], 'Security Camera', 'Raspberry pi security camera update', 'img2.jpg')
            Mails += 1
    timer(15)
    Mails = 0
    test = 0
    start = False

def timer(zeit):
    print "[*]Thread Timer start.\n"
    time.sleep(zeit)
    print "[*]Timer finished."

# def getProfile(id):
#     conn = sqlite3.connect("Facebase.db")
#     cmd = "SELECT * FROM PeopleData WHERE ID="+str(id)
#     cursor = conn.execute(cmd)
#     profile = None
#     for row in cursor:
#         profile = row
#     conn.close()
#     return profile

while (True):
        global test
        global start
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray,1.3,5)
        # yes = eye_detector.detectMultiScale(gray, 1.3, 5)
        #smile = smile_detector.detectMultiScale(gray, 9.3, 8)
        #print test
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
            # id, conf=rec.predict(gray[y:y+h,x:x+w])
           # profile = getProfile(id)
            if(test == 0 and start == False):
                test = test + 1
                frame = cap.read()[1]
                cv2.imwrite(filename='img2.jpg', img=frame)
            #     cv2.cv.PutText(cv2.cv.fromarray(img),"Name: " + str(profile[1]),(x,y+h+20),font,255);
            #     cv2.cv.PutText(cv2.cv.fromarray(img),"Age: " + str(profile[2]),(x,y+h+40),font,255);
            #     cv2.cv.PutText(cv2.cv.fromarray(img),"Gender: " + str(profile[3]),(x,y+h+60),font,255);
            # else:
            #     continue
            #cv2.cv.PutText(cv2.cv.fromarray(img),"Smile: ",(x,y+h+80),font,255);
            # for(ex,ey,ew,eh) in eyes:
            #     cv2.rectangle(img, (ex,ey), (ex+ew,ey+eh), (0,255,0),2)
                #for(sx,sy,sw,sh) in smile:
                    #cv2.rectangle(img, (sx,sy), (sx+sw,sy+sh), (255,0,0), 2)
                    #cv2.cv.PutText(cv2.cv.fromarray(img),"Smile: True",(x,y+h+80),font,255);
        if(test == 1 and start == False):
            start = True
            test = test + 1
            start_new_thread(sendMails, ())

        cv2.imshow('Frame', img);
        if(cv2.waitKey(1) == ord('q')):
            break;

cap.release()
cv2.destroyAllWindows()
