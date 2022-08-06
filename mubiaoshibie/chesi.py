import cv2
import numpy as np

o = cv2.imread('2.jpg')
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary,
 cv2.RETR_TREE,
 cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
#hull = cv2.convexHull(cnt,returnPoints = False)
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])           # 得到的是索引，要再轮廓中选出来
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(o,start,end,[0,0,255],2)
    cv2.circle(o,far,5,[255,0,0],-1)

cv2.imshow('result',o)
cv2.waitKey(0)
cv2.destroyAllWindows()
