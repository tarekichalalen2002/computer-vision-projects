import cv2
import PoseEstimationModule as pm
import time
import numpy as np
from helpers import verifyStance
# ________________________________________________________________________________________ Alternating biceps curls _______________________________________________________________________________________




cap = cv2.VideoCapture(0)


wCam = 1080
hCam = 720
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
detector = pm.PoseDetector()
maxAngle = 160
minAngle = 60
repCounter = 0
right_up = False
right_isTooExtended = False
right_isTooFlexed = False
left_up = False
left_isTooExtended = False
left_isTooFlexed = False


while True:
    success, img = cap.read()
    img = detector.findPose(img, draw=False)
    lmList = detector.findPosition(img, draw=False)
    cv2.putText(img, f'Reps: {str(repCounter)}', (50, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    if right_isTooExtended:
        cv2.putText(img, 'You are extending too much', (50, 150), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
    if right_isTooFlexed:
        cv2.putText(img, 'You are flexing too much', (50, 150), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
    if len(lmList) != 0:
        # right_shoulder_angle = detector.getAngle(img, 24, 12, 11)
        # left_shoulder_angle = detector.getAngle(img, 12, 11, 23)
        # right_hip_angle = detector.getAngle(img, 23, 24, 12)
        # left_hip_angle = detector.getAngle(img, 11, 23, 24)
        # if verifyStance(right_shoulder_angle, left_shoulder_angle, right_hip_angle, left_hip_angle):
        #     img = wait_adjust_stance_img



        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (lmList[13][1], lmList[13][2]), 15, (0, 0, 255), cv2.FILLED)
        right_angle = detector.getAngle(img, 16, 14, 12)
        left_angle = detector.getAngle(img, 15, 13, 11)
        # Adding logic to count reps, The rep is counted when the arm is down and then right_up
        if right_angle <= minAngle:
            if not right_up:
                repCounter += 1
                right_up = True
        if right_angle >= maxAngle and right_up:
            if right_up:
                right_up = False

        # capturing the case when the arm is too extended
        if right_angle > 170:
            right_isTooExtended = True
        if right_isTooExtended and right_angle < 160:
            right_isTooExtended = False

        # capturing the case when the arm is too flexed
        if right_angle < 40:
            right_isTooFlexed = True
        if right_isTooFlexed and right_angle > 50:
            right_isTooFlexed = False

        # Adding logic to count reps, The rep is counted when the arm is down and then left_up
        if left_angle <= minAngle:
            if not left_up:
                repCounter += 1
                left_up = True
        if left_angle >= maxAngle and left_up:
            if left_up:
                left_up = False
                
        # capturing the case when the arm is too extended
        if left_angle > 170:
            left_isTooExtended = True
        if left_isTooExtended and left_angle < 160:
            left_isTooExtended = False
    

        bar = np.interp(right_angle, (minAngle, maxAngle), (100, 650))
        cv2.rectangle(img, (50, 100), (85, 650), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(bar)), (85, 650), (0, 255, 0), cv2.FILLED)
        
        
    cv2.imshow("Image", img)
    cv2.waitKey(7)