import cv2
import numpy as np
back = np.zeros((200,200),np.uint8)
img2 = np.zeros((200,200),np.uint8)

back[20:120, 20:120] = 255
img2[80:180, 80:180] = 255
#非运算(相反颜色)
# img = cv2.bitwise_not(back)
# cv2.imshow("img",img)
# cv2.waitKey(0)
#与运算(同为白则白，否则为黑)
# img = cv2.bitwise_and(back,img2)
# cv2.imshow("img",img)
# cv2.waitKey(0)
#或与异或(或or(融合，交集为白),异或xor(交集为黑))
img = cv2.bitwise_xor(back,img2)
cv2.imshow("img",img)
cv2.waitKey(0)
