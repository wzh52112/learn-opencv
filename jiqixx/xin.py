import cv2
import numpy as np

cap = cv2.VideoCapture('2.flv')

while cap.isOpened():
    ret, frame = cap.read()
    eye = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_righteye_2splits.xml")
    eyes = eye.detectMultiScale(frame, 1.1, 5)
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    #cv2.resizeWindow("frame", 1960, 1080)
    cv2.namedWindow("frame", 0)
    cv2.imshow('frame', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()