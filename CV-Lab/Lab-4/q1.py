import cv2 as cv

img = cv.imread('Res/fish_cat.jpg')

img = cv.resize(img, dsize=(img.shape[1] // 2, img.shape[0] // 2))

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Original Image', grey)
cv.waitKey(0)

threshold_value, bin = cv.threshold(grey, type=cv.THRESH_BINARY, thresh=120, maxval=255)
cv.imshow('Image', bin)
cv.waitKey(0)

threshold_value, bin = cv.threshold(grey, type=cv.THRESH_BINARY_INV, thresh=120, maxval=255)
cv.imshow('Image', bin)
cv.waitKey(0)

threshold_value, bin = cv.threshold(grey, type=cv.THRESH_TOZERO, thresh=120, maxval=255)
cv.imshow('Image', bin)
cv.waitKey(0)

threshold_value, bin = cv.threshold(grey, type=cv.THRESH_TOZERO_INV, thresh=120, maxval=255)
cv.imshow('Image', bin)
cv.waitKey(0)

threshold_value, bin = cv.threshold(grey, type=cv.THRESH_TRUNC, thresh=120, maxval=255)
cv.imshow('Image', bin)
cv.waitKey(0)

threshold_value, bin = cv.threshold(grey, type=cv.THRESH_OTSU, thresh=10, maxval=255)
cv.imshow('Image', bin)
cv.waitKey(0)

cv.destroyAllWindows()
