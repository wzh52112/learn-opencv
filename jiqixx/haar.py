import cv2
import numpy as np

#第一步，创建haar级联器
facer = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
eye = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
#第二步，导入人脸识别的图片并将其灰度化
img = cv2.imread('1.jpg')
#gray = cv2.cvtCoLor(img,cv2.COLOR_BGR2GRAY)
#第三步，进行人脸识别
#[[x,y,W,h]]
faces = facer.detectMultiScale(img, 1.1, 5)
i = 0
for (x,y,w,h) in faces:

    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_img = img[y:y+h,x:x+h]
    eyes = eye.detectMultiScale(roi_img, 1.1, 5)
    for (x, y, w, h) in eyes:
        cv2.rectangle(roi_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
    i = i+1
    winname = 'face' +str(i)
    cv2.imshow(winname,roi_img)
cv2.imshow("img",img)
cv2.waitKey()
