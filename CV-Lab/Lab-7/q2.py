import cv2
import numpy as np
import glob

# Define the dimensions of the checkerboard
CHECKERBOARD = (12, 12)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 0.0001)

# Create vectors to store 3D and 2D points
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane
valid_images = []

# Define world coordinates for 3D points
objp = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[0, :, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
prev_img_shape = None

# Extracting path of individual image stored in a given directory
images = glob.glob('./Res/calib_example/*.tif')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD,
                                             cv2.CALIB_CB_ADAPTIVE_THRESH +
                                             cv2.CALIB_CB_FAST_CHECK +
                                             cv2.CALIB_CB_NORMALIZE_IMAGE)

    # If successful, add object points and image points
    if ret:
        valid_images.append(img.copy())

        objpoints.append(objp)

        # Refine pixel coordinates for given 2D points
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)

        cv2.imshow("Image", img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

# Perform camera calibration
h, w = img.shape[:2]
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Reproject points to verify calibration
for i in range(len(objpoints)):
    # Project 3D points to 2D points
    imgpoints_reproj, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)

    # Get the original image points
    original_points = imgpoints[i].reshape(-1, 2)
    reprojected_points = imgpoints_reproj.reshape(-1, 2)

    # Draw the original and reprojected points
    img = valid_images[i]
    for point in original_points:
        cv2.circle(img, list(map(int, point)), 5, (0, 255, 0), 2)  # Green for original points

    for point in reprojected_points:
        cv2.circle(img, list(map(int, point)), 2, (0, 0, 255), -1)  # Blue for reprojected points

    # Display the image with points
    cv2.imshow('Reprojection Verification', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
