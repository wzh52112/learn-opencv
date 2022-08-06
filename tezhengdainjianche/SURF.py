import cv2
import numpy as np
#python3.6
#读文件
img = cv2. imread('123.jpg')
#灰度化
gray = cv2. cvtColor(img, cv2.COLOR_BGR2GRAY)
#创建sift对象
surf = cv2.xfeatures2d.SURF_create()
#进行检测
kp,des = surf.detectAndCompute(gray, None)#none为区域设置
# print(des[0])
#绘制keypoints|
cv2.drawKeypoints(gray, kp, img)
cv2.imshow('img', img)
cv2.waitKey(0)
