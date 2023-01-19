import numpy as np
import cv2 as cv

img = cv.imread("shroomish.png")

width = img.shape[0]
height = img.shape[1]

prompt_tl = "Enter top-left coord (0 " + str(width) + "): "
prompt_br = "Enter bottom-right coord (0 " + str(height) + "): "

tl = list(map(int, input(prompt_tl).split()))
br = list(map(int, input(prompt_br).split()))

# img_selection = img[tl[0]:br[0], tl[1]:br[1]]
cv.rectangle(img, (tl[0], tl[1]), (br[0], br[1]), (0, 0, 255))

cv.imshow("shroomish", img)
cv.waitKey(0)

cv.destroyAllWindows()
