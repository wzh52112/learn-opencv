import cv2
import numpy as np

#检测高度
line_high = 1000
cars = []
offset = 118
carno = 0
def center(x,y,w,h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x+x1
    cy = y+y1

    return cx,cy

cap = cv2.VideoCapture("345.mp4")
bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG(history=200)
#形态学
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))
while True:
    ret, frame = cap.read()
    if ret == True:
        # 灰度化
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 去噪
        blur = cv2.GaussianBlur(frame, (11, 11), 5)
        # 去背景
        mask = bgsubmog.apply(frame)
        #腐蚀
        erode = cv2.erode(mask,kernel,iterations = 5)
        #膨胀
        dilate = cv2.dilate(erode,kernel)
        #闭操作，去小方块
        close = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
        close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)
        #查找轮廓
        cnts,h = cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        cv2.line(frame,(10,line_high),(1200,line_high),(255,255,0),3)
        for (i,c) in enumerate(cnts):
            (x,y,w,h) = cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            #过滤车辆
            isValid = (w >= 1) and (h >= 1)
            if (not isValid):
                continue
            #有效车辆
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cpoint = center(x,y,w,h)
            cars.append(cpoint)
            for (x,y) in cars: #要有一条线，有范围6，从数组减去。
                if (y<line_high -offset)and(y>line_high+offset):
                    carno+=1
                    cars.remove((x,y))
                    print(carno)
        cv2.putText(frame,"Cars,Count:" + str(carno),(1500,160),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
        cv2.namedWindow("video", 0)
        cv2.resizeWindow("video", 1920, 1080)
        cv2.imshow("video", frame)
    key = cv2.waitKey(1)
    if (key == 27):
        break
cap.release()
cv2.destroyAllWindows()
