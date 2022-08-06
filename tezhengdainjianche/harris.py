import cv2
import numpy as np
blockSize = 2
ksize = 3
k = 0.04
img = cv2.imread('123.jpg')
#灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Harris角点检测
dst = cv2.cornerHarris(gray, blockSize, ksize, k)
#Harris角点的展示
img[dst>0.01*dst.max()] = [0,0,255]
cv2.imshow("harris",img)
cv2.waitKey()