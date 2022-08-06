import cv2
import numpy as np
back = cv2.imread("12.jpg")
smallcat = cv2.imread("123.jpg")
#图片融合addWeighted(A图片,alpha权重, B图片,bate权重,gamma静态权重)
result = cv2.addWeighted(smallcat,0.7,back,0.3,0)
cv2.imshow("result",result)
cv2.waitKey()
