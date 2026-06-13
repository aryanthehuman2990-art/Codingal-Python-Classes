import cv2
import numpy as np
import matplotlib.pyplot as plt

my_image=cv2.imread("C:/Users/ARYAN CHHABRA/Downloads/website.jpg")
def displayer(my_image, title):
    plt.imshow(cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

changer= cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)
displayer(changer,"GREYSCALE IMAGE " )

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
