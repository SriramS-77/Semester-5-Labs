import numpy as np
import cv2 as cv

img = cv.imread("./Res/dog.jpeg")

img = cv.resize(img, dsize=(img.shape[1]//5, img.shape[0]//5))

cv.imshow('frame', img)
cv.waitKey(0)

grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey frame', grey_img)
cv.waitKey(0)

k = 3

avg_filter = np.array([[1/k**2] * k] * k)
np.astype(avg_filter, np.uint8)
avg_filter_img = cv.filter2D(grey_img, kernel=avg_filter, ddepth=-1)
cv.imshow('Average Filter', avg_filter_img)
cv.waitKey(-1)

unsharp_mask = grey_img - avg_filter_img
cv.imshow('Unsharp mask', unsharp_mask)
cv.waitKey(-1)

result = cv.bitwise_and(grey_img, unsharp_mask)
cv.imshow('Result', result)
cv.waitKey(-1)

cv.destroyAllWindows()
