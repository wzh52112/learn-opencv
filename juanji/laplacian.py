import cv2
import numpy as np
img = cv2.imread("123.jpg")
dst = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("o",dst)
cv2.waitKey()