import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    key = cv2.waitKey(1)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_img, low_red, high_red)
    red = cv2.bitwise_and(img, img, mask=red_mask)
    
    low_blue = np.array([100, 50, 50])
    high_blue = np.array([140, 255, 255])
    blue_mask = cv2.inRange(hsv_img, low_blue, high_blue)
    blue = cv2.bitwise_and(img, img, mask=blue_mask)

    low_green = np.array([40, 40, 40])
    high_green = np.array([80, 255, 255])
    green_mask = cv2.inRange(hsv_img, low_green, high_green)
    green = cv2.bitwise_and(img, img, mask=green_mask)
    
    
    cv2.imshow("green", green)
    cv2.imshow("blue", blue)
    cv2.imshow("red", red)
    cv2.imshow("COLOR SELECTOR", hsv_img)
    if key == 27 or key == ord('q'):
        break