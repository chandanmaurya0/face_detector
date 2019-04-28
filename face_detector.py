# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:22:56 2019

@author: Chandan Mauray
"""

import cv2
fae_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = fae_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for (x,y,w,h) in faces:
        roi_gray=gray[y:y+h,x:x+w]
        #img_item ="my_img.png"
        #cv2.imwrite(img_item,roi_gray)
        color=(255,0,0)
        stoke=2
        end_cord_x =x+w
        end_cord_y =y+h
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stoke)
    cv2.imshow("frame",frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break;
        
cap.release()
cv2.destroyAllWindows()