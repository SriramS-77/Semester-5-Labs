import numpy as np
import cv2 as cv

img = cv.imread("../Res/dog.jpeg")

img = cv.resize(img, dsize=(img.shape[1]//5, img.shape[0]//5))

cv.imshow('frame', img)
cv.waitKey(0)

grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey frame', grey_img)
cv.waitKey(0)

# cv.imwrite("../Res/grey_dog.jpeg", grey_img)

vert_filter = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
vert_filter_img = cv.filter2D(grey_img, kernel=vert_filter, ddepth=-1)
cv.imshow('vertical edges', vert_filter_img)
cv.waitKey(-1)

border_mask = cv.bitwise_xor(np.ones(grey_img.shape, dtype=vert_filter_img.dtype), vert_filter_img)
border_img = cv.bitwise_xor(grey_img, vert_filter_img)
cv.imshow('Bordered greyscale', border_img)
cv.waitKey(-1)

horiz_filter = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
horiz_filter_img = cv.filter2D(grey_img, kernel=horiz_filter, ddepth=-1)
cv.imshow('horizontal edges', horiz_filter_img)
cv.waitKey(0)

diagonal_filter = np.array([[-2, -1, 0],
                            [-1, 0, 1],
                            [0, 1, 2]])
diagonal_filter_img = cv.filter2D(grey_img, kernel=diagonal_filter, ddepth=-1)
cv.imshow('Diagonal edges', diagonal_filter_img)
cv.waitKey(0)


k = 9

blur_filter = np.array([[1/k**2] * k] * k)
blur_filter_img = cv.filter2D(grey_img, kernel=blur_filter, ddepth=-1)
cv.imshow('Average Blur', blur_filter_img)
cv.waitKey(0)

cv.destroyAllWindows()
