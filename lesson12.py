import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw TEXT in image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

# lets see 
plt.imshow(img)
plt.show()
