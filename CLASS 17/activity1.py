# BEGIN

# IMPORT OpenCV library as cv2
import cv2
import matplotlib as  plt
import numpy as np
# IMPORT NumPy as np
my_image=cv2.imread("C:/Users/ARYAN CHHABRA/Downloads/website.jpg")
# DEFINE function apply_color_filter(image, filter_type):
def apply_color_filter(image, filter_type):
    
# """

# Apply a specific color filter to the given image and return the result.

# """

# CREATE a copy of the input image called filtered_image
    filtered_image=image.copy()
# IF filter_type == "original":
    if filter_type=="red_tint":
# RETURN the unmodified copy of the image
        filtered_image[:,:,0]=0
        filtered_image[:,:,1]=0
# ELSE IF filter_type == "red_tint":
    elif filter_type=="blue_tint":
        filtered_image[:,:,1]=0
        filtered_image[:,:,2]=0
    elif filter_type=="greem_tint":
        filtered_image[:,:,0]=0
        filtered_image[:,:,2]=0


# ELSE IF filter_type == "increase_red":
    elif filter_type=="increase_red":
# INCREASE the red channel intensity by +50 using cv2.add
        filtered_image[:,:,2]=cv2.add(filtered_image[:,:,2],50)
        
# (Ensures pixel values do not overflow beyond 255)

# ELSE IF filter_type == "decrease_blue":
    elif filter_type == "decrease_blue":
        filtered_image[:,:,1]=cv2.subtract(filtered_image[:,:,1],50)
# DECREASE the blue channel intensity by -50 using cv2.subtract

# (Ensures pixel values do not go below 0)

# RETURN filtered_image
    return filtered_image
# # MAIN SCRIPT EXECUTION

# SET image_path = "example.jpg" # File path of input image

# LOAD the image using cv2.imread

# IF image could not be loaded:
if my_image is None:
    print("image not found")
# PRINT error message "Image not found!"

# ELSE:
else:
    print(" options are o,r,g,b,i,d,e")
    filter_type="orignal"
    while True:

    # RESIZE the image to width=1200, height=800
        cv2.resize(my_image,(1500, 800))
    # INITIALIZE filter_type = "original" # Default filter
       
    # PRINT key options fzxor the user:
        calling= apply_color_filter(my_image, filter_type)
        cv2.imshow("edited image",calling)
        key =cv2.waitKey(0)& 0xFF
        if key== ord("o"):
            filter_type="orignal"
        elif key==ord("r"):
            filter_type="red_tint"
        elif key==ord("b"):
            filter_type="blue_tint"
        elif key==ord("g"):
            filter_type="green_tint"
        elif key==ord("i"):
            filter_type="increase_red"
        elif key== ord("d"):
            filter_type="decrease_blue"
        elif key== ord("e"):
            break
        else:
            print("option chosen is not vaid")
cv2.destroyAllWindows()
        

# o - Original
    
# r - Red Tint

# b - Blue Tint

# g - Green Tint

# i - Increase Red Intensity

# d - Decrease Blue Intensity

# q - Quit

# WHILE True (loop continuously until user exits):

# CALL apply_color_filter(image, filter_type) → filtered_image

# DISPLAY filtered_image in a window titled "Filtered Image"

# WAIT for user key input

# IF key == 'o':

# SET filter_type = "original"

# ELSE IF key == 'r':

# SET filter_type = "red_tint"

# ELSE IF key == 'b':

# SET filter_type = "blue_tint"

# ELSE IF key == 'g':

# SET filter_type = "green_tint"

# ELSE IF key == 'i':

# SET filter_type = "increase_red"

# ELSE IF key == 'd':

# SET filter_type = "decrease_blue"

# ELSE IF key == 'q':

# PRINT "Exiting..."

# BREAK the loop

# ELSE:

# PRINT "Invalid key! Please use 'o', 'r', 'b', 'g', 'i', 'd', or 'q'."

# CLOSE all OpenCV windows

# END