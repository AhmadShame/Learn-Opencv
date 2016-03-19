import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# video recorder
fourcc = cv2.cv.CV_FOURCC('X','V','I','D')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# record video
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('video stream',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
