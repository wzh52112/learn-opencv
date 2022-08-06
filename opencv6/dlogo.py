import cv2
import numpy as np
dog = cv2.imread("123.jpg")
logo = cv2.imread("2.jpg")
mask = cv2.imread("2.jpg")
roi = dog[0:155,0:374]
tmp = cv2.bitwise_and(roi,mask)
dog[0:155,0:374] = tmp
cv2.imshow("o",dog)
cv2.waitKey(0)