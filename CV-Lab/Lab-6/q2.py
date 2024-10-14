import numpy as np
import cv2 as cv

IMAGE_PATH = "./Res/people.webp"

img = cv.imread(IMAGE_PATH)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Initiate ORB detector
orb = cv.ORB_create()

# find the keypoints with ORB
kp, des = orb.detectAndCompute(gray, None)

print(kp[0])
print(des.shape)

# draw only keypoints location,not size and orientation
img = cv.drawKeypoints(gray, kp, img)

cv.imshow('ORB', img)
cv.waitKey(0)

cv.destroyAllWindows()

IMAGE_PATH_1 = "./Res/people.webp"
IMAGE_PATH_2 = "./Res/rotated.jpeg"

gray1 = cv.imread(IMAGE_PATH_1, cv.IMREAD_GRAYSCALE)
gray2 = cv.imread(IMAGE_PATH_2, cv.IMREAD_GRAYSCALE)

orb = cv.ORB_create()

kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# ratio test as per Lowe's paper
good = []
for i,(m,n) in enumerate(matches):
    if m.distance > 0.75 * n.distance:
        good.append([m])

img3 = cv.drawMatchesKnn(gray1, kp1, gray2, kp2, good, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv.imshow('Matches', img3)
cv.waitKey(0)

cv.destroyAllWindows()
