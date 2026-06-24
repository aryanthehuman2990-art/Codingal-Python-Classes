#############################################

# GESTURE-BASED SCROLL CONTROL - PSEUDO CODE

#############################################

# ---------------------------------------------------

# STEP 1: Import required libraries
import cv2
import time
import mediapipe as mp
import pyautogui
# - Library for capturing video from webcam

# - Library for time management (FPS, delays)

# - Library for controlling scroll on the system

# - Library for hand tracking and gesture detection

# ---------------------------------------------------

# ---------------------------------------------------

# STEP 2: Initialize hand tracking model

# - Set maximum number of hands to detect (e.g., 1)
Hands=mp.solutions.hands
hands = Hands.Hands(max_num_hands=1,min_detection_confidence=0.7)
draw = mp.solutions.drawing_utils

# - Set minimum detection confidence (e.g., 0.7)

# - Prepare utility for drawing hand landmarks

# ---------------------------------------------------

# ---------------------------------------------------

# STEP 3: Define configuration values

# - SCROLL_SPEED = how much to scroll per gesture
SCROLL_SPEED=100
# - SCROLL_DELAY = how many seconds to wait between scroll actions
SCROLL_DELAY=0.5
# - CAM_WIDTH, CAM_HEIGHT = resolution of the camera feed
CAM_WIDTH, CAM_HEIGHT =200,400
# ---------------------------------------------------

# ---------------------------------------------------

# STEP 4: Create gesture detection function

# - Input: landmarks of detected hand + handedness (Left/Right hand)
def gesture_detection(landmarks,handedness):
    fingers=[]
    tp=[Hands.HandLandmark.INDEX_FINGER_TIP,Hands.HandLandmark.MIDDLE_FINGER_TIP, Hands.HandLandmark.RING_FINGER_TIP,Hands.HandLandmark.PINKY_TIP]
    thumb_tp=landmarks.landmark[Hands.HandLandmark.THUMB_TIP]
    thumb_ip=landmarks.landmark[Hands.HandLandmark.THUMB_IP]
    for i in tp:
        if landmarks.landmark[i].y<landmarks.landmark[i-2].y:
            fingers.append(1)
        
        if(handedness=="Right"and thumb_tp.x>thumb_ip.x)or (handedness=="Left"and thumb_tp.x<thumb_ip.x):
            fingers.append(1)
    return"scroll_up" if sum(fingers)==5 else "scroll_down" if len(fingers)==0 else "none"
    
            
# - Process:

# 1. Check which fingers are extended

# - Compare fingertip landmark with its lower joint

# - If fingertip is above joint => finger extended

# 2. Check thumb position (different for Left vs Right hand)

# 3. Count how many fingers are extended

# - Output:

# - If all 5 fingers extended => return "scroll_up"

# - If 0 fingers extended => return "scroll_down"

# - Otherwise => return "none"

# ---------------------------------------------------
# ---------------------------------------------------

# STEP 5: Setup webcam capture

# - Open webcam stream
cap=cv2.VideoCapture(0)
cap.set(3,CAM_WIDTH)
cap.set(3,CAM_HEIGHT)
# - Set frame width and height

# - Initialize variables for scroll timing and FPS tracking
scrolltime=0
fps=0
print("q for exit")

# ---------------------------------------------------

# ---------------------------------------------------

# STEP 6: Main loop

# - While webcam is open:
while cap.isOpened():
    ok, img = cap.read()
    if not ok:
        break
    
    img = cv2.flip(img, 1)
    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    gesture,handedness="None","unknown"
    if res.multi_hand_landmarks :
        for i, hand in zip(res.multi_hand_landmarks, res.multi_handedness):
            label =hand.classification[0].label
            gesture= gesture_detection(i,label)
            draw.draw_landmarks(img, i, Hands.HAND_CONNECTIONS) 
            if (time.time()-scrolltime)>SCROLL_DELAY:
                if gesture=="scroll_up":
                    pyautogui.scroll(SCROLL_SPEED)
                elif gesture=="scroll_down":
                    pyautogui.scroll(-SCROLL_SPEED)
                last_scroll=time.time()
    fps1 = 1/(time.time()-fps) if (time.time()-fps) > 0 else 0 
    fps=time.time()
    cv2.putText( img,f" fps:{fps1}" ,(10,110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
       
    cv2.imshow("Webcam Control Window", img) 
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27 :
        break

cap.release()
cv2.destroyAllWindows()

                # 1. Capture a frame from the webcam

# 2. Convert frame to correct format (RGB)

# 3. Flip image horizontally for mirror effect

# 4. Run hand detection on the frame

# 5. If a hand is detected:

# a. Get hand landmarks and handedness (Left/Right)

# b. Call gesture detection function

# c. Draw detected landmarks on the frame

# d. If enough time has passed since last scroll:

# i. If gesture = scroll_up => perform system scroll up

# ii. If gesture = scroll_down => perform system scroll down

# iii. Update last scroll time

# 6. Calculate FPS (frames per second)

# 7. Overlay FPS, handedness, and gesture info on the frame

# 8. Show frame in a window

# 9. If user presses quit key (e.g., 'q'), break loop

# ---------------------------------------------------

# ---------------------------------------------------

# STEP 7: Cleanup

# - Release webcam resource

# - Close any display windows

# ---------------------------------------------------