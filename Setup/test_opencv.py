import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])


    #define range of red color in HSV
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([179, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask_blue  = cv.inRange(hsv, lower_blue, upper_blue)
    mask_red   = cv.inRange(hsv, lower_red1, upper_red1) | cv.inRange(hsv, lower_red2, upper_red2)

    #combine to show red and blue at the same time
    mask = mask_blue |  mask_red

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()