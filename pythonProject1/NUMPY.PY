import numpy as np
import cv2

img = np.zeros((480, 640, 3),np.uint8)
#
# print(img[100,100])
# count = 0
# while count <200:
#     img[count,100] = [255,0,255]
#     count = count+1

roi = img[100:400, 100:600]
roi[:,2] = [0,0,255]
roi[200,10:200]=[0,255,0]
cv2.imshow("img",roi)
key = cv2.waitKey(0)
if key & 0xFF == ord("q"):
    cv2.destroyALLWindows()

