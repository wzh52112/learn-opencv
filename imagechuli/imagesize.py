import  cv2
import  numpy as np
dog = cv2.imread("12.jpg")
print(dog.shape)
new = cv2.resize(dog,(3840*2,2160*2),interpolation=cv2.INTER_NEAREST)
cv2.imshow("1",new)
cv2.imshow("2",dog)
cv2.waitKey(0)