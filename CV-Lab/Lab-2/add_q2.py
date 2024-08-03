import time
import cv2 as cv
import numpy as np

GAMMA_VALUES = [.1, .5, 1, 5, 10]
# [.1, .25, .5, .75, 1, 1.1, 1.25, 1.5, 1.75, 2]

img = cv.imread("./Res/resized_dog.jpeg")

img = cv.resize(img, dsize=(img.shape[1]//2, img.shape[0]//2))

for gamma in GAMMA_VALUES:
    gamma_transformed = np.astype(255 * (img / 255) ** gamma, np.uint8)
    cv.imshow('Gamma_'+str(gamma), gamma_transformed)

cv.waitKey(0)
cv.destroyAllWindows()

dark = cv.imread("./Res/dark_forest.jpg")
dark = cv.resize(dark, dsize=(200, 200))
cv.imshow("Original Dark", dark)

gamma = .5
dark = np.astype(255 * (dark / 255) ** gamma, np.uint8)
cv.imshow('Dark', dark)

cv.waitKey(0)
cv.destroyAllWindows()

bright = cv.imread("./Res/unfixed_bright_img.jpeg")

cv.imshow("Original Bright", bright)

gamma = 3
bright = np.astype(255 * (bright / 255) ** gamma, np.uint8)
cv.imshow('Altered Bright', bright)

cv.waitKey(0)
cv.destroyAllWindows()
