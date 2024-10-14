import cv2 as cv
import imutils

IMG_PATH = "Res/people.webp"

img = cv.imread(IMG_PATH, cv.IMREAD_GRAYSCALE)

img = imutils.rotate(img, 90)

print(img.shape)
cv.imshow("Image", img)
cv.waitKey(0)

cv.destroyAllWindows()

cv.imwrite('Res/rotated.jpeg', img)
