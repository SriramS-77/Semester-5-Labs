import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def show_histogram(img):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.title("Histogram of image to get values for contrast stretching")
    plt.show()

def piecewiseTransform(pix, r1, s1, r2, s2):
    if 0 <= pix and pix < r1:
        return (s1 / r1) * pix
    elif r1 <= pix < r2:
        return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2) / (255 - r2)) * (pix - r2) + s2

img = cv.imread("./Res/contrast_stretching.jpeg")

show_histogram(img)

r1 = 0 # 10
s1 = 20
r2 = 80
s2 = 255 # 230

pixel_transform = np.vectorize(piecewiseTransform)

contrast_stretched = pixel_transform(img, r1, s1, r2, s2)
contrast_stretched = np.astype(contrast_stretched, np.uint8)

cv.imshow("Original", img)
cv.imshow("Contrast Stretched", contrast_stretched)

cv.waitKey(0)
cv.destroyAllWindows()
