# Load the image
import cv2
image=cv2.imread("C:/Users/ARYAN CHHABRA/Downloads/website.jpg")
# Resize the window to a specific size without resizing the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Create a resizable window
Resize=cv2.resize(gray_image, (224, 224))
# Set the window size to 800x500 (width x height)
# Display the image in the resized window
cv2.imshow("NEW IMAGE", Resize)
# Wait for a key press
key=cv2.waitKey(10000)
if key== ord("s"):

    cv2.imwrite("greyscale_resized_image.jpg",Resize)
    print("Image saved as grayscale_resized_image.jpg")
else:
    print("Image is not saved")

# Close the window
cv2.destroyAllWindows()
# Print image properties
print(f"Image Dimensions:{Resize.shape}")
# Height, Width, Channels
