# --------------------------------------------------------------
# Import necessary libraries for:
# 1. Image processing (OpenCV)
# 2. Numerical operations (NumPy)
# 3. Displaying images (Matplotlib)
import cv2
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------------------

# --------------------------------------------------------------
# Define a utility function to display images using Matplotlib.
# 1. Set up the figure size.
# 2. Check if image is grayscale or color.
# 3. Convert color images from BGR to RGB for correct rendering.
# 4. Set the plot title and hide the axis.
# 5. Display the image on the screen.
my_image=cv2.imread("C:/Users/ARYAN CHHABRA/Downloads/website.jpg")
def displayer(my_image, title):
    plt.imshow(cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
# --------------------------------------------------------------

# --------------------------------------------------------------
# Define the main interactive function for edge detection.
# 1. Load an image from a specified path.
# 2. Convert it to grayscale.
# 3. Show the grayscale image to the user.
# 4. Present a menu of operations:
#    a) Sobel Edge Detection
#    b) Canny Edge Detection
#    c) Laplacian Edge Detection
#    d) Gaussian Smoothing
#    e) Median Filtering
#    f) Exit
# 5. Prompt the user to pick an option.
# 6. Perform the chosen operation and display the result.
# 7. Repeat until the user decides to exit.
changer= cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)
displayer(changer,"GREYSCALE IMAGE " )
# --------------------------------------------------------------

# --------------------------------------------------------------
# Sobel Edge Detection:
# 1. Calculate Sobel filters along the x and y directions.
# 2. Convert both results to 8-bit images.
# 3. Combine them using bitwise OR.
# 4. Display the combined edge map.
print("(1)SOBEL EDGE")
print("(2)CANNY EDGE")
print("(3)LAPLACIAN EDGE")
print("(4)GAUSSIAN SMOOTHING")
print("(5)MEDIAN FILTERING")
print("(6)EXIT")

while True:
    choice=int(input("SELECT ONE"))
    if choice==1:
        sobelx=cv2.Sobel(changer, cv2.CV_64F ,1 ,0, ksize=3)
        sobely=cv2.Sobel(changer, cv2.CV_64F ,0 ,1, ksize=3)
        sobelxy=cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
        displayer(sobelxy, "SOBEL IMAGE")
    elif choice==2:
        cannyx=10
        cannyy=100
        cannyxy=cv2.Canny(changer,cannyx, cannyy)
        displayer(cannyxy, "CANNY IMAGE")
    elif choice==3:
        laplacian=cv2.Laplacian(changer, cv2.CV_64FC2 )
        displayer(np.abs(laplacian).astype(np.uint8), "LAPLACIAN IMAGE")
    elif choice==4:
        kernalsize=5
        gause=cv2.GaussianBlur(my_image,(kernalsize,(kernalsize)),0)
        displayer(gause, "GAUSSIAN BLUR IMAGE")
    elif choice==5:
        kernalsize=11
        gause=cv2.medianBlur(my_image,kernalsize)
        displayer(gause, "MEDIAN FILTERING")
    elif choice==6:
        print("EXITING")
        break
    else:
        print("invalid choice")

# --------------------------------------------------------------

# --------------------------------------------------------------
# Canny Edge Detection:
# 1. Ask for lower and upper thresholds.
# 2. Apply Canny edge detection, which:
#    - Smooths the image with a Gaussian filter.
#    - Finds intensity gradients.
#    - Applies non-maximum suppression.
#    - Uses double-thresholding and edge tracking.
# 3. Display the detected edges.

# --------------------------------------------------------------

# --------------------------------------------------------------
# Laplacian Edge Detection:
# 1. Apply the Laplacian operator (second derivative).
# 2. Take the absolute value of the result to handle negative gradients.
# 3. Convert to 8-bit for display.
# 4. Show the resulting edges

# --------------------------------------------------------------

# --------------------------------------------------------------
# Gaussian Smoothing:
# 1. Prompt the user for a kernel size (odd number).
# 2. Apply GaussianBlur with the specified kernel.
# 3. Display the smoothed image, which helps reduce noise.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Median Filtering:
# 1. Prompt the user for a kernel size (odd number).
# 2. Apply medianBlur, which replaces each pixel with the median of neighbors.
# 3. This helps remove salt-and-pepper noise while preserving edges.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Exit:
# 1. Print a message confirming exit.
# 2. Break out of the interactive loop.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Make a call to the interactive function with the path to an image.
# e.g., interactive_edge_detection("example.jpg")
# This is where the program starts running and awaits user input.
# --------------------------------------------------------------
