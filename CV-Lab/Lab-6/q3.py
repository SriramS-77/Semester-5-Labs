import cv2
import numpy as np

IMAGE_PATH_1 = "./Res/people.webp"
IMAGE_PATH_2 = "./Res/rotated.jpeg"

# Load images
image1 = cv2.imread(IMAGE_PATH_1)
image2 = cv2.imread(IMAGE_PATH_2)

# Convert to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Detect ORB keypoints and descriptors
orb = cv2.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

# Match descriptors using BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(descriptors1, descriptors2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw matches (optional)
matched_image = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches[:30], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('Matches', matched_image)
cv2.waitKey(0)

# Extract location of good matches
points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt

# Estimate homography using RANSAC
H, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

# Print the homography matrix
print("Homography Matrix:\n", H)

# Optionally, warp one image to the other using the estimated homography
height, width, _ = image2.shape
warped_image = cv2.warpPerspective(image1, H, (width, height))

# Display the results
cv2.imshow('Warped Image', warped_image)
cv2.imshow('Original Image 2', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
