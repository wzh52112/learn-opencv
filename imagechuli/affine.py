import cv2
import numpy as np
dog = cv2.imread('123.jpg')
h,w,ch = dog.shape
M = np.float32([[1,0,100],[0,1,0]])
print(M)
new = cv2.warpAffine(dog, M,(w,h))
cv2.imshow("new",new)
cv2.waitKey()