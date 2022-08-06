import cv2
import numpy as np
cap = cv2.VideoCapture('123.mp4' )
mog = cv2.createBackgroundSubtractorMOG2(history=50000000,detectShadows=False)
while(True):
    ret, frame = cap.read()
    fgmask = mog.apply(frame)
    cv2.imshow( 'img' ,fgmask)
    k = cv2.waitKey(10)
    if k ==27:
        break
cap.release( )
cv2.destroyAllWindows( )
