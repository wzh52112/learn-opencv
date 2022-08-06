import  cv2
import  numpy as np
img = cv2.imread("123.jpg")
# kernel = np.ones((5,5),np.float32)/25
# dst = cv2.filter2D(img,-1,kernel)
# dst = cv2.blur(img,(5,10))
dst = cv2.boxFilter(img,-1,(5,5),True)
cv2.imshow("dst",dst)
#cv2.imshow("img",img)
cv2.waitKey()