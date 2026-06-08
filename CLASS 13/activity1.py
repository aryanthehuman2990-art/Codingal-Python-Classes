# Load the image
import cv2
image=cv2.imread("C:/Users/ARYAN CHHABRA/Downloads/website.jpg")
# Resize the window to a specific size without resizing the image
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
# Create a resizable window
cv2.resizeWindow("Loaded Image", 800, 500)
# Set the window size to 800x500 (width x height)
# Display the image in the resized window
cv2.imshow("Loaded Image", image)
# Wait for a key press
cv2.waitKey(10000)
# Close the window
cv2.destroyAllWindows()
# Print image properties
print(f"Image Dimensions:{image.shape}")
# Height, Width, Channels