import cv2
import numpy as np
#img = cv2.imread("3,jpg")
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
print(kernel)