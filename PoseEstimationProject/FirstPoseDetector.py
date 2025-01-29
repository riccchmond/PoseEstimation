import cv2
import time
import PoseModule as pm

cap = cv2.VideoCapture('PoseVideos/5.mp4')
pTime = 0
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img)
    print(lmList)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_ITALIC, 2, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(20)
