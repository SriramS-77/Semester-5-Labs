import cv2 as cv
import numpy as np

img = cv.imread("Res/knives.webp")

img = cv.resize(img, dsize=(img.shape[1] // 3, img.shape[0] // 3))

canny = cv.Canny(img, 75, 150)

detectedlines = cv.HoughLinesP(canny, 1, np.pi/180, 60, maxLineGap=30)

for line in detectedlines:
    x0, y0, x1, y1 = line[0]
    cv.line(img, (x0, y0), (x1, y1), (0, 0, 250), 1)

cv.imshow("HoughTransform", img)
cv.waitKey(0)
cv.destroyAllWindows()
