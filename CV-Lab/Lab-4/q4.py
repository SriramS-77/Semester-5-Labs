import numpy as np
import cv2 as cv

img = cv.imread('Res/objects.jpg')
img = cv.resize(img, dsize=(img.shape[1] // 4, img.shape[0] // 4))

cv.imshow('Input', img)
cv.waitKey(0)

Z = img.reshape((-1, 3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 5
ret, label, center = cv.kmeans(Z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv.imshow('Output', res2)

cv.waitKey(0)
cv.destroyAllWindows()
