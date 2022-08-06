import cv2
import numpy as np
dog = cv2.imread('123.jpg')
h,w,ch = dog.shape
#变换矩阵
#逆时针旋转
# new = cv2.getRotationMatrix2D((w/2,h/2),15,0.3)
# new2 = cv2.warpAffine(dog,new,(int(w*0.5),int(h*0.5)))
#print(new2.shape)
#三点变换
src = np.float32([[400,300],[800,300],[400,1000]])
dst = np.float32([[200,400],[600,500],[150,1100]])
M = cv2.getAffineTransform(src,dst)
new2 = cv2.warpAffine(dog,M,(w,h))
cv2.imshow("new",new2)
cv2.waitKey()