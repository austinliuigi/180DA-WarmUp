import numpy as np
import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    _, frame = capture.read()
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    lower_bound = np.array([35, 50, 50])
    upper_bound = np.array([150, 225, 225])
    mask = cv.inRange(frame_hsv, lower_bound, upper_bound)
    result = cv.bitwise_and(frame, frame, mask = mask)
    result_grayscale = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
    result_grayscale_blurred = cv.blur(result_grayscale, (3,3))

    edges = cv.Canny(result_grayscale_blurred, 100, 200)
    # contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    _, thresh = cv.threshold(result_grayscale, 50, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        max_contour = max(contours, key = cv.contourArea)
        x,y,w,h = cv.boundingRect(max_contour)
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)

    # for contour in range(len(contours)):
    #     x,y,w,h = cv.boundingRect(contours[contour])
    #     cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)

    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break

capture.release()
