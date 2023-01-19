import numpy as np
import cv2 as cv

shroomish = cv.imread("shroomish.png")
shroomish_hsv = cv.cvtColor(shroomish, cv.COLOR_BGR2HSV)
shroomish_grayscale = cv.cvtColor(shroomish, cv.COLOR_BGR2GRAY)

# lower_bound = np.array([10, 0, 10])
# upper_bound = np.array([50, 75, 255])
# mask = cv.inRange(shroomish_hsv, lower_bound, upper_bound)
# result = cv.bitwise_and(shroomish, shroomish, mask = mask)
# result_grayscale = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
lower_bound = np.array([25, 10, 25])
upper_bound = np.array([200, 175, 225])
mask = cv.inRange(shroomish_hsv, lower_bound, upper_bound)
result = cv.bitwise_and(shroomish, shroomish, mask = mask)
result_grayscale = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
result_grayscale_blurred = cv.blur(result_grayscale, (3,3))

edges = cv.Canny(result_grayscale_blurred, 100, 200)
contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for contour in range(len(contours)):
    x,y,w,h = cv.boundingRect(contours[contour])
    cv.rectangle(shroomish, (x,y), (x+w, y+h), (0,255,0),2)

cv.imshow("mask", mask)
cv.waitKey(0)
cv.imshow("result", result)
cv.waitKey(0)
cv.imshow("result_grayscale", result_grayscale)
cv.waitKey(0)
cv.imshow("result_grayscale_blurred", result_grayscale_blurred)
cv.waitKey(0)
cv.imshow("edges", edges)
cv.waitKey(0)

cv.drawContours(shroomish, contours, -1, (0, 0, 255), 2)
cv.imshow("contours", shroomish)
cv.waitKey(0)

cv.destroyAllWindows()
