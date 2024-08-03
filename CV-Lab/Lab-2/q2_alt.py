import cv2 as cv
from skimage.exposure import match_histograms

src = cv.imread("./Res/lion.jpg")
ref = cv.imread("./Res/tiger.jpg")

src = cv.resize(src, dsize=(ref.shape[1], ref.shape[0]))

matched = match_histograms(src, ref, channel_axis=2)

cv.imshow('Src', src)
cv.imshow('Ref', ref)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('Histogram Matched', matched)

cv.waitKey(0)
cv.destroyAllWindows()
