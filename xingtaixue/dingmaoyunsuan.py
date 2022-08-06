import cv2
import numpy as np
img = cv2.imread("5.jpg")
kernel = np.ones((25,25),np.uint8)
dst = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow("img",img)
cv2.imshow("dst",dst)
#cv2.imshow("dst1",dst1)
cv2.waitKey()