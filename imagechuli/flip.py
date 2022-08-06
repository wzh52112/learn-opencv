import cv2
import numpy as np
dog = cv2.imread('123.jpg')
new = cv2.flip(dog, 1)#1,0,-1
cv2.imshow('new',new)
cv2.imshow("dog",dog)
cv2.waitKey(0)
