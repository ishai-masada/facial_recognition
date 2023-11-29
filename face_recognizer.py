import cv2

vid_path = 'videos/IMG_5094.MOV'

# Load the cascade from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load Camera Input
vid = cv2.VideoCapture(vid_path)
#vid = cv2.VideoCapture(1)
#print(vid.isOpened())

while True:
    # Input the frame from the video
    _, frame = vid.read()

    # Convert it from color to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find the face in the frame
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Draw a rectangle around the face
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('video', 500, 500)
    cv2.imshow('video', frame)
    
    # Don't know what this is yet
    key = cv2.waitKey(1)
    if key == 27 and 0xff == ord('q'):
        break

