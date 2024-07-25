import imutils
import cv2 as cv

img = cv.imread("../Res/dog.jpeg")

img = cv.resize(img, dsize=(img.shape[1]//5, img.shape[0]//5))

cv.imshow('Resized frame', img)
cv.waitKey(0)

img = imutils.rotate(img, 315)

cv.imshow('Rotated frame', img)
cv.waitKey(0)

cv.destroyAllWindows()