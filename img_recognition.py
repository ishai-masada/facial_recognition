import cv2

# Image path
img_path = "images/vish.jpg"

# Image name 
#img_name = "The Elon"
img_name = "Vishy"

# Load the face cascade from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the image
image = cv2.imread(img_path)

# Convert it from color to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find the face in the frame
face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)

# Draw a rectangle around the face
for (x, y, w, h) in face:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)

# Create named window
cv2.namedWindow(img_name, cv2.WINDOW_NORMAL)

# Set the dimensions of the window
cv2.resizeWindow(img_name, 600, 600)

# Set the window position
cv2.moveWindow(img_name, 350, 150)

# Display the image
cv2.imshow(img_name, image)

# Wait for the user to press a key to close the window
cv2.waitKey(0)

# Destroy the window
cv2.destroyWindow(img_name)

