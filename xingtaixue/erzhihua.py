import cv2
src = cv2.imread("123.jpg")
img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
ret,dst = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
cv2.imshow("o",dst)
cv2.waitKey()