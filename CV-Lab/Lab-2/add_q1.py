import cv2 as cv
import numpy as np

img = cv.imread("./Res/resized_dog.jpeg")

img = cv.resize(img, dsize=(img.shape[1]//2, img.shape[0]//2))

inverted_img = np.astype(255 - img, np.uint8)

c = 255 / (np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)
log_transformed = np.astype(log_transformed, np.uint8)

cv.imshow("Inverted", inverted_img)
cv.imshow("Log transform", log_transformed)

cv.waitKey(0)
cv.destroyAllWindows()
