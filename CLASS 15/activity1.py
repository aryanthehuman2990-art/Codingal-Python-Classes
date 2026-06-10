import cv2
import matplotlib.pyplot as plt

# Step 1: Load the Image
  # User-provided image path
  # Convert BGR to RGB for correct color display with matplotlib
my_image=cv2.imread("C:/Users/ARYAN CHHABRA/Downloads/website.jpg")
changer= cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
# Get image dimensions
height,width,channel=changer.shape

# Step 2: Draw Two Rectangles Around Interesting Regions
# Rectangle 1: Top-left corner
rect1_width, rect1_height=150,150
top_left1=(20,20)
bottom_right1=(top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(changer, top_left1, bottom_right1, (0, 255, 255), 3)

  # Yellow rectangle
  # Fixed 20 pixels padding from top-left
# Yellow rectangle

# Rectangle 2: Bottom-right corner
  # 20 pixels padding
  # Magenta rectangle
rect2_width, rect2_height=200,150
top_left2=(width-rect2_width-20, height - rect2_height - 20)
bottom_right2=(top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(changer, top_left2, bottom_right2, (0, 255, 255), 3)
# Step 3: Draw Circles at the Centers of Both Rectangles
   # Filled green circle
    # Filled red circle
center1_x=top_left1[0]+rect1_width//2
center1_y=top_left1[1]+rect1_height//2
cv2.circle(changer, (center1_x, center1_y), 15, (255, 255, 255), -1)

center2_x=top_left2[0]+rect2_width//2
center2_y=top_left2[1]+rect2_height//2
cv2.circle(changer, (center2_x, center2_y), 15, (0, 255, 0), -1)


# Step 4: Draw Connecting Lines Between Centers of Rectangles
cv2.line(changer, (center1_x, center1_y), (center2_x, center2_y), (0, 255, 0), 3)

# Step 5: Add Text Labels for Regions and Centers
cv2.putText(changer,"region1",
(top_left1[0], top_left1[1] -10),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2,cv2.LINE_AA)
cv2.putText(changer,"region2",
(top_left2[0], top_left2[1] -10),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2,cv2.LINE_AA)
cv2.putText(changer,"center1",
(center1_x-40, center1_y +40),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2,cv2.LINE_AA)
cv2.putText(changer,"center1",
(center2_x-40, center2_y +40),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2,cv2.LINE_AA)
# Step 6: Add Bi-Directional Arrow Representing Height
  # Start near the top-right
  # End near the bottom-right
arrow_start=(width-20, 20)
arrow_end=(width+20, -20)
cv2.arrowedLine(changer, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)

cv2.arrowedLine(changer, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
# Draw arrows in both directions
  # Downward arrow
 # Upward arrow

# Annotate the height value
plt.imshow(changer)

plt.axis('off')

plt.show()

# Step 7: Display the Annotated Image
