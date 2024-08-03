import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def show_histogram(img, title="Title"):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.title(title)
    plt.show()


img = cv.imread("./Res/dog.jpeg")
img = cv.resize(img, dsize=(img.shape[1]//5, img.shape[0]//5))

grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#cv.imshow("frame", grey_img)
#cv.waitKey(0)
#cv.destroyAllWindows()

show_histogram(grey_img, "Original Histogram")

equ = cv.equalizeHist(grey_img)
cv.imshow('Original - Image', grey_img)
cv.imshow('Equalized Histogram - Image', equ)

cv.waitKey(0)
cv.destroyAllWindows()

show_histogram(equ, "Equalized Histogram")
