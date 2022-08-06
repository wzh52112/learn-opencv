import cv2
import numpy as np
#角点的最大数,值为0表示无限制
maxCorners = 0
#小于1.0的正数, 一般在0.01-0.1之间
qualityLevel = 0.01
#角之间最小欧式距离,忽略小于此距离的点。
minDistance = 10
#感兴趣的区域
#mask =
#检测窗口
#biockSize =
#是否使用Harris算法
#useHarrisDetector = False
#权重，默认是0.04
#k = 0.04
img = cv2.imread('123.jpg')
#灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Shi-Tomasi角点检测
dst = cv2.goodFeaturesToTrack(gray, maxCorners, qualityLevel, minDistance)
dst = np.int0(dst)
#Shi-Tomasi角点的展示
for i in dst:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(255,0,0),-1)

cv2.imshow("harris",img)
cv2.waitKey()