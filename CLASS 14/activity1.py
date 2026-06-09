# Color Conversions and Cropping
import cv2
import matplotlib.pyplot as plt
my_image=cv2.imread("C:/Users/ARYAN CHHABRA/Downloads/website.jpg")

# Convert BGR to RGB
changer= cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
plt.imshow(changer)
plt.title("my image")
plt.show()
# Convert to Grayscale
changer= cv2.cvtColor(my_image, cv2.COLOR_RGB2GRAY)
plt.imshow(changer)
plt.title("my GREY image")
plt.show()
# Cropping the image
my_image= my_image[100:300, 200:400]
plt.imshow(my_image)
plt.show()
# Assume we know the region we want: rows 100 to 300, columns 200 to 400

