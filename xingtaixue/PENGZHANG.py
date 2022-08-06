import cv2
import numpy as np
img = cv2.imread("3.jpg")
kernel = np.ones((7,7),np.uint8)
dst = cv2.dilate(img,kernel,iterations=5)
dst1 = cv2.erode(dst,kernel,iterations=5)
cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.imshow("dst1",dst1)
cv2.waitKey()