import numpy as np
import cv2
import PoseEstimationModule as pm
import time

cap = cv2.VideoCapture(0)
pTime = 0

wCam = 1080
hCam = 720

cap.set(3, wCam)
cap.set(4, hCam)

detector = pm.PoseDetector()

minAngle = 60
maxAngle = 150

pBest_speed = 0
best_speed = 0

right_extended = False
left_extended = False

punches_thrown = 0

pTime = 0

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img)
    cv2.putText(img, f'Punches Thrown: {str(punches_thrown)}', (50, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    if len(lmList) != 0:
        right_angle = detector.getAngle(img, 16, 14, 12)
        left_angle = detector.getAngle(img, 15, 13, 11)

        if right_angle >= maxAngle:
            if not right_extended:
                punches_thrown += 1
                right_extended = True
        if left_angle >= maxAngle:
            if not left_extended:
                punches_thrown += 1
                left_extended = True

        if right_angle < minAngle and right_angle:
            right_extended = False
        if left_angle < minAngle and left_angle:
            left_extended = False
        

    cv2.imshow("Image", img)
    cv2.waitKey(5)


    # cTime = time.time()
    # fps = 1/(cTime-pTime)
    # pTime = cTime