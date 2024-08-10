import numpy as np
import cv2 as cv

img = cv.imread("./Res/dog.jpeg")

img = cv.resize(img, dsize=(img.shape[1]//5, img.shape[0]//5))

grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey frame', grey_img)
cv.waitKey(0)

gradient_filter = [[-1, 1],
                   [-1, 1]]


res = cv.filter2D(grey_img, -1, np.array(gradient_filter))
cv.imshow('Gradients', res)
cv.waitKey(-1)

cv.destroyAllWindows()
