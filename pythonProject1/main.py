import cv2


cv2.namedWindow("img", cv2.WINDOW_NORMAL)
img = cv2.imread("shenfenzheng.jpg")
while True:
    cv2.imshow("img",img)
    key = cv2.waitKey(0)
    print("2")
    print(key)
    print(ord("2"))
    if(key & 0xFF == ord("2")):
        print("执行")
        exit()
        cv2.destroyALLWindows()
    elif(key & 0xFF == ord("1")):
        cv2.imwrite("C:\\Users\\wangzhonghan\\Desktop\\pythonProject1\\123.png",img)
    else:
        print(key)
print("jiesu")
cv2.destroyALLWindows()
