# Import required libraries

import cv2

import numpy as np

# Function to apply selected image filter

def apply_filter(image, ftype):

# Copy original frame to avoid overwriting source data
    copy1=image.copy()
    if ftype=="red_tint":
        copy1[:,:,0]=0
        copy1[:,:,1]=0
    elif ftype=="green_tint":
        copy1[:,:,0]=0
        copy1[:,:,2]=0
    elif ftype=="blue_tint":
        copy1[:,:,1]=0
        copy1[:,:,2]=0
    elif ftype=="sobel":
        changer=cv2.cvtColor(copy1, cv2.COLOR_BGR2GRAY)
        sobelx=cv2.Sobel(changer, cv2.CV_64F ,1 ,0, ksize=3)
        sobely=cv2.Sobel(changer, cv2.CV_64F ,0 ,1, ksize=3)
        sobelxy=cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
        copy1=cv2.cvtColor(sobelxy, cv2.COLOR_GRAY2BGR)
    elif ftype=="canny":
        changer=cv2.cvtColor(copy1, cv2.COLOR_BGR2GRAY)
        cannyx=10
        cannyy=100
        cannyxy=cv2.Canny(changer, cannyx, cannyy)
        copy1=cv2.cvtColor(cannyxy, cv2.COLOR_GRAY2BGR)
    elif ftype=="medianblur":
        kernalsize=11
        copy1=cv2.medianBlur(copy1,kernalsize)
    return copy1 
    
def main():
    cap=cv2.VideoCapture(0)
    print("r for red /n b for blue /n g for green /n s for sobel /n c for canny /n m for medianblur /n q for quit")
    
    
    ftype="original"
    
    while True:  
        ret,frame=cap.read()
        if not ret:
            print("Not able to capture image")
        caller= apply_filter(frame, ftype)
        cv2.imshow("editor", caller )
        key=cv2.waitKey(1)& 0xFF
        if key==ord("r"):
                ftype="red_tint"
        elif key==ord("b"):
            ftype="blue_tint"
        elif key==ord("g"):
            ftype="green_tint"
        elif key==ord("s"):
            ftype="sobel"
        elif key==ord("c"):
            ftype="canny"
        elif key==ord("m"):
            ftype="medianblur"
        elif key==ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()
    



# Initialize default webcam (index 0)


# Check if camera opened successfully


# Set default filter mode to original


# Print control keys instructions


# Live frame processing loop


# Capture frame-by-frame


# Stop if frame cannot be retrieved


# Apply the active filter


# Display output window


# Read keypress (1ms delay)


# Switch filter mode based on key mapping:

# 'r'=Red, 'g'=Green, 'b'=Blue, 's'=Sobel, 'c'=Canny, 't'=Cartoon


# 'q' key to exit loop



# Release camera and close all GUI windows



# Execute main function

