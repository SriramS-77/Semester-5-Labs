import math

import cv2
import numpy as np
import cv2 as cv
from math import *

def get_gauss_value(x, y, sigma):
    val = 1 / (2 * pi * pow(sigma, 2))
    val *= math.pow(math.e, (-.5 / sigma ** 2) * (x ** 2 + y ** 2))
    return val


def get_gaussian_kernel(size, sigma):
    data = np.random.randn(10000)

    vals, x_distribution, y_distribution = np.histogram2d(data, data, bins=size-1, density=True)
    res = np.matmul(x_distribution.reshape(-1, 1), y_distribution.reshape(1, -1))
    res = (res ** -1)
    res /= res.sum()
    print(res, res.sum())
    np.astype(res, np.uint8)
    return res


def get_box_filter(size):
    arr = np.array([[1]*size]*size) / size ** 2
    np.astype(arr, np.uint8)
    return arr


img = cv.imread("./Res/dog.jpeg")

img = cv.resize(img, dsize=(img.shape[1]//5, img.shape[0]//5))
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey frame', grey_img)
cv.waitKey(-1)

box_img = cv2.filter2D(grey_img, -1, get_box_filter(3))

cv.imshow('Box Filter', box_img)
cv.waitKey(-1)

gauss_img = cv2.filter2D(grey_img, -1, get_gaussian_kernel(7, 1))

cv.imshow('Gauss Filter', gauss_img)
cv.waitKey(-1)

cv.destroyAllWindows()
