import cv2 as cv
from skimage.exposure import match_histograms

src = cv.imread("./Res/resized_dog.jpeg")
ref = cv.imread("./Res/cropped_dog.jpeg")

matched = match_histograms(src, ref, channel_axis=2)

cv.imshow('Src', src)
cv.imshow('Ref', ref)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('Histogram Matched', matched)

cv.waitKey(0)
cv.destroyAllWindows()
