import cv2
import numpy as np
dog = cv2.imread("123.jpg")
#图的加法运算就是矩阵的加法运算
#因此两张图必须相等
img = np.ones((1080, 1920, 3),np.uint8) * 2
cv2.imshow("orig",dog)
#cv2.imshow("orig2",img)
#add加法
#subtract减法
#multiply乘法
#divide除法
result = cv2.multiply(dog,img)
cv2.imshow("result",result)
result2 = cv2.divide(result,img)
cv2.imshow("result2",result2)
cv2.waitKey(0)