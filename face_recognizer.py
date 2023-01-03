import cv2

vid_path = 'IMG_5094.MOV'
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load Camera Input
vid = cv2.VideoCapture(vid_path)
#vid = cv2.VideoCapture(0)
#print(vid.isOpened())

while True:
    _, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('video', frame)
    
    key = cv2.waitKey(1)

    if key == 27 and 0xff == ord('q'):
        break

