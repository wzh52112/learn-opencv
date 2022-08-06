import cv2

def callback():
    pass

cv2.namedWindow("clor", cv2.WINDOW_NORMAL)

img = cv2.imread("C:\\Users\\wangzhonghan\\Downloads\\BIZHI\\wallhaven-3z9yd9.jpg")

colorspaces = [cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2RGBA,
               cv2.COLOR_BGR2YUV,cv2.COLOR_BGR2HSV,cv2.COLOR_BGR2LAB]

cv2.createTrackbar("cur color", "clor", 0, len(colorspaces),callback)

while True:
    index = cv2.getTrackbarPos("cur color", "clor")
    cvt_img = cv2.cvtColor(img, colorspaces[index])
    cv2.imshow("clor", cvt_img)
    key = cv2.waitKey(10)
    if key & 0xFF == ord("1"):
        break
cv2.destroyALLWindows()
