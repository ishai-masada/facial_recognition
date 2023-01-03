import cv2

bah = "images/rick.webp"
heh = cv2.imread(bah)
cv2.namedWindow('heh', cv2.WINDOW_NORMAL)
cv2.resizeWindow('heh', 500, 500)
cv2.imshow('heh', heh)

cv2.waitKey(0)
