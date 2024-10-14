import cv2
import numpy as np
import glob

# Define the dimensions of the checkerboard
CHECKERBOARD = (12, 12)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 0.0001)

# Create vectors to store 3D and 2D points
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

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
        objpoints.append(objp)

        # Refine pixel coordinates for given 2D points
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)

    cv2.imshow('img', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# Perform camera calibration
h, w = img.shape[:2]
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Print intrinsic parameters
print("\nCamera matrix (Intrinsic Parameters):")
print(mtx)

print("\nDistortion coefficients:")
print(dist)

print("\n\nExtrinsic parameters for each imager:\n")

# Extrinsic parameters (rotation and translation vectors)
for i in range(len(rvecs)):
    print(f"\nRotation Vector {i}:")
    print(rvecs[i])
    print(f"\nTranslation Vector {i}:")
    print(tvecs[i])

"""
# Example of using the intrinsic parameters to undistort an image
undistorted_img = cv2.undistort(img, mtx, dist)
cv2.imshow('Undistorted Image', undistorted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""