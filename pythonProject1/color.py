import cv2

image = cv2.imread('C:\\Users\\wangzhonghan\\Downloads\\BIZHI\\wallhaven-3z9yd9.jpg')
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.imwrite("1_gray.jpg", gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.imwrite("1_hsv.jpg", hsv)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)
cv2.imwrite("1_lab.jpg", lab)

if (cv2.waitKey(0) == 27):
    cv2.destroyAllWindows()