import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw polylines
pts = np.array([[1,20],[50,60],[100,150],[200,20]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),5)


# lets see 
plt.imshow(img)
plt.show()
