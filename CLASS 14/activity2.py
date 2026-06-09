#  Rotating and Adjusting Brightness
import cv2
import matplotlib.pyplot as plt
import numpy as np
my_image=cv2.imread("C:/Users/ARYAN CHHABRA/Downloads/website.jpg")
changer= cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
# Rotate the image by 45 degrees around its center
  # rotate by 45 degrees

(h, w) = my_image.shape[:2]

center=(w//2, h//2)
rot=cv2.getRotationMatrix2D(center, 45, 1.0 )
war=cv2.warpAffine(my_image, rot, (h,w))
plt.imshow(war)
plt.show()
# Increase brightness by adding 50 to all pixel values
brightness= np.ones(my_image.shape, dtype="uint8")*50
# Use cv2.add to avoid negative values or overflow
bad=cv2.add(my_image, brightness)
plt.imshow(bad)
plt.show()
