import cv2
import numpy as np
img = cv2.imread("123.png")
#高度 宽度 通道数
print(img.shape)
#占用空间（高度*宽度*通道数）
print(img.size)
#图像中每个元素位深
print(img.dtype)