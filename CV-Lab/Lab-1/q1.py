import cv2 as cv

img = cv.imread("../Res/dog.jpeg")

img = cv.resize(img, dsize=(img.shape[1]//5, img.shape[0]//5))

cv.imshow('frame', img)
cv.waitKey(0)

cv.destroyAllWindows()

cv.imwrite("../Res/duplicate_dog.jpeg", img)
