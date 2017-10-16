import numpy as np
import cv2
import sqlite3
from Mail import sendMail
from thread import start_new_thread
from threading import Thread
import time

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
cap = cv2.VideoCapture(0);
#rec = cv2.createLBPHFaceRecognizer();
#rec.load("recognizer\\trainningData.yml")
id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,1,.5,0,2,1)

test = 0
start = False

##def getProfile(id):
##    conn = sqlite3.connect("Facebase.db")
##    cmd = "SELECT * FROM PeopleData WHERE ID="+str(id)
##    cursor = conn.execute(cmd)
##    profile = None
##    for row in cursor:
##        profile = row
##    conn.close()
##    return profile

def sendMails():
    global start
    global test
    print "[*]Thread Mail start.\n"
    sendMail('[Mail]', 'Security Camera', 'Raspberry pi security camera update', 'img2.jpg')
    sendMail('[Mail]', 'Security Camera', 'Raspberry pi security camera update', 'img2.jpg')
    timer(15)
    test = 0
    start = False
    
def timer(zeit):
    print "[*]Thread Timer start.\n"
    time.sleep(zeit)
    print "[*]Timer finished."

while (True):
    global test
    global start
    ret, img = cap.read()
    res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    img = res
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,1.3,5)
    #eyes = eye_detector.detectMultiScale(gray, 1.3, 5)
    #smile = smile_detector.detectMultiScale(gray, 9.3, 8)
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
        if(test == 0 and start == False):
                test = test + 1
                frame = cap.read()[1]
##        id, conf=rec.predict(gray[y:y+h,x:x+w])
##        profile = getProfile(id)
##        if(profile != None):
##            cv2.cv.PutText(cv2.cv.fromarray(img),"Name: " + str(profile[1]),(x,y+h+20),font,255);
##            cv2.cv.PutText(cv2.cv.fromarray(img),"Age: " + str(profile[2]),(x,y+h+40),font,255);
##            cv2.cv.PutText(cv2.cv.fromarray(img),"Gender: " + str(profile[3]),(x,y+h+60),font,255);
##        else:
##            cv2.cv.PutText(cv2.cv.fromarray(img),"Name: Unknown", (x,y+h+20),font,255);
##            cv2.cv.PutText(cv2.cv.fromarray(img),"Age: Unknown", (x,y+h+40),font,255);
##            cv2.cv.PutText(cv2.cv.fromarray(img),"Gender: Unknown", (x,y+h+60),font,255);
##        #cv2.cv.PutText(cv2.cv.fromarray(img),"Smile: ",(x,y+h+80),font,255);
##        for(ex,ey,ew,eh) in eyes:
##            cv2.rectangle(img, (ex,ey), (ex+ew,ey+eh), (0,255,0),2)
##            #for(sx,sy,sw,sh) in smile:
##                #cv2.rectangle(img, (sx,sy), (sx+sw,sy+sh), (255,0,0), 2)
##                #cv2.cv.PutText(cv2.cv.fromarray(img),"Smile: True",(x,y+h+80),font,255);
    if(test == 1 and start == False):
        start = True
        test = test + 1
        start_new_thread(sendMails, ())
    cv2.imshow('Frame', img);
    if(cv2.waitKey(1) == ord('q')):
        break;
cap.release()
cv2.destroyAllWindows()    
