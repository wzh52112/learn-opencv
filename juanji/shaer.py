import cv2
import numpy as np
img = cv2.imread("123.jpg")
dst = cv2.Scharr(img,cv2.CV_64F,1,0)
im = cv2.Scharr(img,cv2.CV_64F,0,1)
dst1 = im + dst
cv2.imshow("o",dst1)
cv2.waitKey()