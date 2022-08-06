import cv2
import numpy as np
img = cv2.imread('123.jpg')
src = np.float32([[100,1100],[2100,1100],[0,4000],[2500,3900]])
dst = np.float32([[0,0],[2300,0],[0,3000],[2300,3000]])
M = cv2.getPerspectiveTrainsform(src,dst)
cv2.warpPerspective(img,M,(2300,3000))
cv2.imshow("o",img)
cv2.imshow("q",new)
cv2.waitKey()