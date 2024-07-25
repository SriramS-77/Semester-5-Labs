import cv2 as cv

img = cv.imread("../Res/dog.jpeg")

img = cv.resize(img, dsize=(img.shape[1]//5, img.shape[0]//5))

w, h = img.shape[1], img.shape[0]

img = cv.rectangle(img, pt1=(2*w//10, 2*h//10), pt2=(8*w//10, 8*h//10), color=(255, 100, 100), thickness=5)

cv.imshow('frame', img)
cv.waitKey(0)

cv.destroyAllWindows()
