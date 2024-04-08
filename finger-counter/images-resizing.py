import cv2
import os

folderPath = "finger-images"
myList = os.listdir(folderPath)
w,h = 250, 180
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    h,w,c = image.shape
    while w > 300 or h > 400:
        image = cv2.resize(image, (w//2, h//2))
    cv2.imwrite(f'{folderPath}/{imPath}', image)