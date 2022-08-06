import cv2
import numpy as np
img = cv2.imread( '3.jpg' )
img2 = cv2.imread( '4.jpg' ,0)
dst = cv2.inpaint(img, img2, 5, cv2.INPAINT_TELEA)
cv2.imshow( 'dst', dst)
cv2.waitKey( )
