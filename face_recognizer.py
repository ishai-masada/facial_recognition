import cv2
import os

path_1 = 'images/elon.jpg'
path_2 = 'images/rick.webp'

img_1 = cv2.imread(path_1)
img_2 = cv2.imread(path_2)

cascade_path = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_path)

# Load Camera
vid = cv2.VideoCapture(0)

if not vid.isOpened():
    print("Cannot open camera")

#while True:
#    ret, frame = capture.read()
    
#    key = cv2.waitKey(1)
