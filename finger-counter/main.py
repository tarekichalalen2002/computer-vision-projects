import os
import cv2
import time
import HandTrackingModule as htm
import numpy as np




cap = cv2.VideoCapture(0)

wCam = 720
hCam = 480

cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

folderPath = "finger-images"
myList = os.listdir(folderPath)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
detector = htm.HandDetector(detectionCon=0.75)
finger_tips = [8, 12, 16, 20]
while True:
    success, img = cap.read()
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    count = 0
    if len(lmList) != 0:
        x4, y4 = lmList[4][1], lmList[4][2]
        x5, y5 = lmList[5][1], lmList[5][2]
        p1, p2 = np.array([x4, y4]), np.array([x5, y5])
        if int(np.linalg.norm(p1 - p2)) > 50:
            count += 1
        for ft in finger_tips:
            if lmList[ft][2] < lmList[ft-1][2]:
                count += 1
    cv2.putText(img, f'finger count: {str(count)}', (10, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    # h,w,c = overlayList[2].shape
    # img[0:h,0:w] = overlayList[2]
    cv2.imshow("Image", img)
    cv2.waitKey(1)