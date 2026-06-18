import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap= cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if not ret:
        print("Not able to capture image")
        break
    changer=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    multiscale=face_cascade.detectMultiScale(changer, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in multiscale: cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, str(len(multiscale)),(10,10), font,1, (255,0,0), 3, cv2.LINE_AA)
    cv2.imshow("detector", frame)
    
    if cv2.waitKey(1)&0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
