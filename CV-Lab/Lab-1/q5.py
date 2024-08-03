import numpy as np
import cv2 as cv

img = cv.imread("./Res/dog.jpeg")

cv.imshow('Original frame', img)
cv.waitKey(0)

img = cv.resize(img, dsize=(img.shape[1]//5, img.shape[0]//5))

cv.imshow('Resized frame', img)
cv.waitKey(0)

cv.destroyAllWindows()
