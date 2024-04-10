import cv2
import PoseEstimationModule as pm
from helpers import verifyStance


img = cv2.imread('side-pose-man.jpg')
detector = pm.PoseDetector()
img = detector.findPose(img, draw=False)
lmlist = detector.findPosition(img, draw=True)
print(lmlist)
if lmlist:
    right_shoulder_angle = detector.getAngle(img, 24, 12, 11)
    left_shoulder_angle = detector.getAngle(img, 12, 11, 23)
    right_hip_angle = detector.getAngle(img, 23, 24, 12)
    left_hip_angle = detector.getAngle(img, 11, 23, 24)

    cv2.putText(img, str(int(right_shoulder_angle)), (lmlist[12][1]-10, lmlist[12][2]+10), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.putText(img, str(int(left_shoulder_angle)), (lmlist[11][1]-10, lmlist[11][2]+10), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.putText(img, str(int(right_hip_angle)), (lmlist[23][1]-10, lmlist[23][2]+10), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.putText(img, str(int(left_hip_angle)), (lmlist[24][1]-10, lmlist[24][2]+10), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    print(verifyStance(right_shoulder_angle, left_shoulder_angle, right_hip_angle, left_hip_angle))
cv2.imwrite("processed-image.jpg",img )


# lmList = detector.findPosition(img, draw=False)