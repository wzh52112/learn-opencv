import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)
#划线
# cv2.line(img,(10,20),(100,400),(0,0,255),3,19)
# cv2.imshow("draw",img)
# cv2.waitKey(0)
#画矩形
# cv2.rectangle(img, (10,10),(100, 100),(0, 0, 255), -1)
# cv2.imshow("draw",img)
# cv2.waitKey(0)
#画圆
# cv2.circle(img,(320, 240), 100, (0, 0, 255))
# cv2.circle(img, (320, 240), 5,(0, 0, 255), -1)
# cv2.imshow("draw",img)
# cv2.waitKey(0)
#画椭圆
# cv2.ellipse(img,(320,240),(100,50),0,0,360,(0,0,255),-1)
# cv2.imshow("draw",img)
# cv2.waitKey(0)
#画多边形
# pts = np.array([(300,10),(150,100),(450,100)],np.int32)
# cv2.polylines(img,[pts],True,(0,0,255))
# cv2.fillPoly(img,[pts],(255,255,0))
# cv2.imshow("draw",img)
# cv2.waitKey()
#绘制文本
# cv2.putText(img, "213", (10, 400), cv2.FONT_HERSHEY_TRIPLEX, 5, (255,45, 0))
# cv2.imshow( 'draw', img )
# cv2.waitKey(0)

