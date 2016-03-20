import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw Ellipse
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)


# lets see 
plt.imshow(img)
plt.show()
