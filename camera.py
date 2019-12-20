import cv2
import numpy
import sys

cam = cv2.VideoCapture(2)

ret, frame = cam.read()
name = ('calib_pics/calib'+sys.argv[1]+'.jpg')
cv2.imwrite(name,frame)
cv2.imshow('frame',frame)

if cv2.waitKey(1) == ord('p') & 0xFF:
    cam.release()
    cv2.destroyAllWindows()
