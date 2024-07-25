import cv2 as cv
import numpy as np

img = cv.imread("../Res/dog.jpeg")

img = cv.resize(img, dsize=(img.shape[1]//5, img.shape[0]//5))

#cv.imshow('frame', img)
#cv.waitKey(0)

#img[0], img[2] = img[2], img[0]

cv.imshow('frame', img)
cv.waitKey(0)

cv.destroyAllWindows()

print("RGB value of 1st pixel: ", img[0][0][2], img[0][0][1], img[0][0][0])
