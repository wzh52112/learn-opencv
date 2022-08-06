#先膨胀
import cv2
import numpy as np
img = cv2.imread("4.jpg")
kernel = np.ones((13,13),np.uint8)
dst = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow("img",img)
cv2.imshow("dst",dst)
#cv2.imshow("dst1",dst1)
cv2.waitKey()