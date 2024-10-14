import numpy as np
import cv2 as cv

IMAGE_PATH = "./Res/people.webp"
IMAGE_PATH_1 = "./Res/people.webp"
IMAGE_PATH_2 = "./Res/rotated.jpeg"

img = cv.imread(IMAGE_PATH)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Greyscale', gray)
cv.waitKey(0)

sift = cv.SIFT_create()

kp, des = sift.detectAndCompute(gray, None)

print(kp[0])
print(des.shape)

img = cv.drawKeypoints(gray, kp, img)

cv.imshow('SIFT', img)
cv.waitKey(0)

cv.destroyAllWindows()



gray1 = cv.imread(IMAGE_PATH_1, cv.IMREAD_GRAYSCALE)
gray2 = cv.imread(IMAGE_PATH_2, cv.IMREAD_GRAYSCALE)

sift = cv.SIFT_create()
orb = cv.ORB_create()

kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=1)

img3 = cv.drawMatchesKnn(gray1, kp1, gray2, kp2, matches, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv.imshow('Matches', img3)
cv.waitKey(0)

cv.destroyAllWindows()
