import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((512,512,3), np.uint8)

#Draw Rectangle
cv2.rectangle(img,(100,100),(250,250),(0,255,0),3)


# lets see 
plt.imshow(img)
plt.show()
