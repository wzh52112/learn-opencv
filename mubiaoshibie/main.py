import cv2
import numpy as np
# def drawShape(src,points):
#     i=0
#     while i < len(points):
#         if(i == len(points) - 1):
#             x,y = points[i][0]
#             x1,y1 = points[0][0]
#             cv2.line(src,(x,y),(x1,y1),(0,255,0),1)
#         else:
#             x, y = points[i][0]
#             x1, y1 = points[i + 1][0]
#             cv2.line(src, (x, y), (x1, y1), (0, 255, 0), 1)
#         i = i + 1
img = cv2.imread("3.jpg")
#变成单通道
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
R,B = cv2.threshold(gray,110,255,cv2.THRESH_BINARY)
#查找轮廓
dst,hierarchy = cv2.findContours(B,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(dst)
#绘制轮廓
points = cv2.drawContours(img,dst,0,(0,0,255),1)
#计算面积
# area = cv2.contourArea(dst[0])
# print("area=%d"%(area))
#计算周长(true闭合，false非闭合)
# len = cv2.arcLength(dst[0],True)
# print("len=%d"%(len))


#多边形逼近
# e = 5
# approx = cv2.approxPolyDP(dst[0],e,True)
# drawShape(img,approx)
# hull = cv2.convexHull(dst[0])
# drawShape(img,hull)
#外界矩阵
#最小
r = cv2.minAreaRect(dst[1])
box = cv2.boxPoints(r)#只取起始点和宽高
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)
#最大
x,y,w,h= cv2.boundingRect(dst[1])
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("dst",img)
cv2.waitKey()
