import cv2
import numpy as np
img = cv2.imread("123.jpg")
dst = cv2.Canny(img,100,200)
cv2.imshow("o",dst)
cv2.waitKey()