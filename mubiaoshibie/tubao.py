import cv2
import numpy as np

def drawShape(src, points):
    i = 0
    while i < len(points):
        if(i == len(points)-1):
            x,y = points[i][0]
            x1,y1 = points[0][0]
            cv2.line(src, (x,y), (x1,y1), (0,255,0), 3)
        else:
            x,y = points[i][0]
            x1,y1 = points[i+1][0]
            cv2.line(src, (x,y), (x1,y1), (0,255,0), 3)
        i = i+1

#读文件
img = cv2.imread('2.jpg')
#转变成单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#二值化,第一个返回值是执行的结果和状态是否成功，第二个返回值才是真正的图片结果
ret,binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
#轮廓查找,第一个返回值是轮廓，第二个是层级
contours, hierarchy =  cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#绘制轮廓
cv2.drawContours(img, contours, 0, (0,0,255), 1)#改变的是img这张图

#多边形逼近,20代表精度，数字越大代表精度越低，approx返回的是点的数组
approx = cv2.approxPolyDP(contours[0], 5, True)
drawShape(img, approx)
print(approx)
print(len(approx))
#凸包
hull = cv2.convexHull(contours[0])
drawShape(img, hull)


cv2.imshow('img',img)
cv2.imshow('binary',binary)
cv2.waitKey(0)
