import cv2
import numpy as np
img = cv2.imread("3.jpg")
kernel = np.ones((7,7),np.uint8)
dst = cv2.erode(img,kernel,iterations=5)
cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey()