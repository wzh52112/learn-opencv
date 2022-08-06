import cv2
import numpy as np
#python3.6
#读文件
img1 = cv2. imread('1.jpg')
img2 = cv2. imread('2.jpg')
#灰度化
g1 = cv2. cvtColor(img1, cv2.COLOR_BGR2GRAY)
g2 = cv2. cvtColor(img2, cv2.COLOR_BGR2GRAY)
#创建sift对象
sift = cv2.xfeatures2d.SIFT_create()
#orb进行检测
kp1,des1 = sift.detectAndCompute(g1, None)#none为区域设置
kp2,des2 = sift.detectAndCompute(g2, None)
# print(des[0])
bf = cv2.BFMatcher(cv2.NORM_L1)
match = bf.match(des1, des2)
img3 = cv2.drawMatches(img1, kp1, img2, kp2, match, None)

#绘制keypoints
# cv2.drawKeypoints(gray, kp, img)
cv2.imshow('img3', img3)
cv2.waitKey(0)
