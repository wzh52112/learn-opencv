# USAGE
# python opencv_haar_cascades.py --cascades cascades

# 导入必要的包
import argparse
import os  # 不同系统路径分隔符
import time  # sleep 2秒

import cv2  # opencv绑定
import imutils
from imutils.video import VideoStream  # 访问网络摄像头

# 构建命令行参数及解析
# --cascades 级联检测器的路径
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascades", type=str, default="cascades",
                help="path to input directory containing haar cascades")
args = vars(ap.parse_args())

# 初始化字典，并保存Haar级联检测器名称及文件路径
detectorPaths = {
    "face": cv2.data.haarcascades +"haarcascade_frontalface_alt2.xml",
    "eyes": cv2.data.haarcascades +"haarcascade_eye.xml",
    "smile": cv2.data.haarcascades +"haarcascade_smile.xml",
}

# 初始化字典以保存多个Haar级联检测器
print("[INFO] loading haar cascades...")
detectors = {}

# 遍历检测器路径
for (name, path) in detectorPaths.items():
    # 加载Haar级联检测器并保存到map
    path = os.path.sep.join([args["cascades"], path])
    detectors[name] = cv2.CascadeClassifier(path)

# 初始化视频流，允许摄像头预热2s
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# 遍历视频流的每一帧
while True:
    # 获取视频流的每一帧，缩放，并转换灰度图
    frame = vs.read()
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用合适的Haar检测器执行面部检测
    faceRects = detectors["face"].detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)

    # 遍历检测到的所有面部
    for (fX, fY, fW, fH) in faceRects:
        # 提取面部ROI
        faceROI = gray[fY:fY + fH, fX:fX + fW]

        # 在面部ROI应用左右眼级联检测器
        eyeRects = detectors["eyes"].detectMultiScale(
            faceROI, scaleFactor=1.1, minNeighbors=10,
            minSize=(15, 15), flags=cv2.CASCADE_SCALE_IMAGE)

        # 在面部ROI应用嘴部检测
        smileRects = detectors["smile"].detectMultiScale(
            faceROI, scaleFactor=1.1, minNeighbors=10,
            minSize=(15, 15), flags=cv2.CASCADE_SCALE_IMAGE)

        # 遍历眼睛边界框
        for (eX, eY, eW, eH) in eyeRects:
            # 绘制眼睛边界框（红色）
            ptA = (fX + eX, fY + eY)
            ptB = (fX + eX + eW, fY + eY + eH)
            cv2.rectangle(frame, ptA, ptB, (0, 0, 255), 2)

        # 遍历嘴部边界框
        for (sX, sY, sW, sH) in smileRects:
            # 绘制嘴边界框（蓝色）
            ptA = (fX + sX, fY + sY)
            ptB = (fX + sX + sW, fY + sY + sH)
            cv2.rectangle(frame, ptA, ptB, (255, 0, 0), 2)

        # 绘制面部边界框（绿色）
        cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH),
                      (0, 255, 0), 2)

    # 展示输出帧
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # 按下‘q’键，退出循环
    if key == ord("q"):
        break

# 清理工作
cv2.destroyAllWindows()
vs.stop()
