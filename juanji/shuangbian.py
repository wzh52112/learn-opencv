import cv2
import numpy as np
img = cv2.imread("123.jpg")
dst = cv2.bilateralFilter(img,70,20,500)
cv2.imshow("o",dst)
cv2.waitKey()