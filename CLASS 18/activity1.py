# Load the pre-trained Haar Cascade Classifier for face detection
import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the default webcam (0)
cap = cv2.VideoCapture(0)
# Capture frame-by-frame
while True:
    ret, frame=cap.read()


# If frame is read correctly, ret will be True     
    if not ret:
        print("FAIL TO CAPTURE IMAGE")
        break
# Convert frame to grayscale (Face detection works better on grayscale)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
# Draw rectangles around the faces
    for (x, y, w, h) in faces: cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
# Blue rectangle with thickness 2
    cv2.imshow("DETECTOR", frame)
# Display the resulting frame

# Break the loop when the 'q' key is pressed
    if cv2.waitKey(1)& 0xFF==ord("q"):
        break

# Release the capture and close any open windows
cap.release()
cv2.destroyAllWindows