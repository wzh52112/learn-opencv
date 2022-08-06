import cv2
import numpy as np
import pytesseract

#第一步，创建haar级联器
plate = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
#第二步，导入人脸识别的图片并将其灰度化
img = cv2.imread('3.jpg')
#gray = cv2.cvtCoLor(img,cv2.COLOR_BGR2GRAY)
#第三步，进行人脸识别
#[[x,y,W,h]]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plates = plate.detectMultiScale(gray, 1.1, 3)
for (x,y,w,h) in plates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
roi = gray[y:y+h,x:x+w]
ret,roi_bin = cv2.threshold(roi,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(pytesseract.image_to_string(roi,lang="eng",config="--psm 8 --oem 3"))
cv2.imshow("img",img)
cv2.imshow("roi_bin",roi_bin)
cv2.waitKey()
