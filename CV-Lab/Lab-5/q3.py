import cv2
import numpy as np
from math import sqrt

def compute_dp(img, octaves_n=3, frames_n=5, k=sqrt(2)):
    img = img.astype('float64')
    img /= 255
    cv2.imshow('Input', img)
    cv2.waitKey(0)
    octave_lst = []
    for octave_i in range(octaves_n):
        octave = []
        sigma = sqrt(2) / 2 * 2 ** octave_i   # Initial sigma
        for frame_i in range(frames_n):
            img_blurred = cv2.GaussianBlur(img, (11, 11), sigma)
            octave.append(img_blurred)
            sigma *= k

        octave_lst.append(octave)

    dp = [[octave_lst[j][i+1] - octave_lst[j][i] for i in range(len(octave_lst[j]) - 1)] for j in range(len(octave_lst))]
    dp = np.array(dp)
    print(dp.shape)
    #for i in dp:
    #    for j in i:
    #        cv2.imshow('Input', j)
    #        cv2.waitKey(0)
    return dp

def detect_kp(dp, thrs=0.03):
    kp = []
    for oct_i in range(dp.shape[0]):
        for i in range(1, dp.shape[2]-1):
            for j in range(1, dp.shape[3]-1):
                patch = dp[oct_i, :, i-1: i+2, j-1: j+2]
                # print(patch.shape)
                if np.max(patch) < thrs:
                    continue

                patch = np.max(patch, axis=1)
                patch = np.max(patch, axis=1)
                idx = np.argmax(patch)

                sigma = sqrt(2) / 2 * (2 ** oct_i) * sqrt(2) ** idx
                kp.append([sigma, i, j])
    return kp

def eliminate_edges(img, kp):
    k = 0.04
    th = 1e-6
    true_kp = []
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    Dxx, Dxy, Dyy = 0, 0, 0
    window_size = 7
    for sigma, x, y in kp:
        for i in range(x - window_size//2, x + window_size//2 + 1):
            for j in range(y - window_size // 2, y + window_size // 2 + 1):
                Dx, Dy = sobel_x[x][y], sobel_y[x][y]
                Dxx += Dx ** 2
                Dxy += Dx * Dy
                Dyy += Dy ** 2
        Dxx, Dxy, Dyy = Dxx / window_size ** 2, Dxy / window_size ** 2, Dyy / window_size ** 2
        h_mat = np.array([[Dxx, Dxy],
                          [Dxy, Dyy]])

        det = np.linalg.det(h_mat)
        trace = np.trace(h_mat)
        res = det - k * (trace ** 2)
        if res > 10:
            true_kp.append([sigma, x, y])
    return true_kp

def draw_keypoints(img, kp):
    img_kp = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for si, x, y in kp:
        cv2.circle(img_kp, (int(y), int(x)), 2, (0, 255, 0), 1)
        # cv2.putText(img_kp, f'{si}', (int(y), int(x) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
    return img_kp


img_path = 'Res/people.webp'
img = cv2.imread(img_path)
cv2.imshow('Input', img)
cv2.waitKey(0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dp = compute_dp(img)

kp = detect_kp(dp)

kp = eliminate_edges(img, kp)
print(len(kp))
img_kp = draw_keypoints(img, kp)

cv2.imshow('Output', img_kp)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Custom Descriptors: {dp.shape}")
