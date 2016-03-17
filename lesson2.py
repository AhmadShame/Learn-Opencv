import numpy as np
import cv2
img = cv2.imread('gift.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:               # wait for Esc key to exit  ([27 =Esc] in ASCII)
     cv2.destroyAllWindows()
elif k == ord('s'):        # wait for 's' key to save and exit
     cv2.imwrite('copygift.png',img)
     cv2.destroyAllWindows()
