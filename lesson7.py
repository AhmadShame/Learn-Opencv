import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# & Don't assign it
cv2.line(img,(0,0),(511,511),(0,0,255),5)

# lets see 
plt.imshow(img)
plt.show()
