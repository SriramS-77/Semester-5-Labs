import numpy as np
import cv2 as cv

img = cv.imread("./Res/dog.jpeg")

img = cv.resize(img, dsize=(img.shape[1]//5, img.shape[0]//5))

grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey frame', grey_img)
cv.waitKey(0)

vertical_edge_filter = [[-1, 0, 1],
                          [-1, 0, 1],
                          [-1, 0, 1]]

horizontal_edge_filter = [[-1, -1, -1],
                          [0, 0, 0],
                          [1, 1, 1]]


v_res = cv.filter2D(grey_img, -1, np.array(vertical_edge_filter))
cv.imshow('Vertical edges', v_res)
cv.waitKey(-1)

h_res = cv.filter2D(grey_img, -1, np.array(horizontal_edge_filter))
cv.imshow('Horizontal edges', h_res)
cv.waitKey(-1)

cv.destroyAllWindows()
