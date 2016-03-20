import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw circle
cv2.circle(img,(250,250), 63, (0,0,255), -1)


# lets see 
plt.imshow(img)
plt.show()
