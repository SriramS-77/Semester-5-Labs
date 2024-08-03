import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./Res/resized_dog.jpeg")

cv.imshow("Original Image", img)

cv.waitKey(0)
cv.destroyAllWindows()

img = img[200:600, 230:570]

cv.imshow("Cropped Image", img)

cv.waitKey(0)
cv.destroyAllWindows()

#cv.imwrite("./Res/cropped_dog.jpeg", img)
