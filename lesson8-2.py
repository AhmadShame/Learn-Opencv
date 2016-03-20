import numpy as np
import cv2
from matplotlib import pyplot as plt

# read image
img =cv2.imread('gift.jpg')

#invert color from B,G,R  to R,G,B
b,g,r = cv2.split(img)       # get b,g,r
img = cv2.merge([r,g,b])     # switch it to rgb

# Draw a diagonal blue line with thickness of 5 px
cv2.rectangle(img,(380,260),(570,460),(255,0,0),3)

# lets see 
plt.imshow(img)
plt.show()

