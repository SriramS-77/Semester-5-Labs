import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def compute_histogram(hsv_img):
    print("Computing histogram...")
    # hist, bin_edges = np.histogram(hsv_img[:, :, 0], bins=10)

    plt.hist(hsv_img[:, :, 0], bins=10)
    plt.title("Histogram with 10 bins")
    plt.show()
    print("Done!")


def segment_red(img, hsv_img):
    lower_mask = hsv_img[:, :, 0] > 0
    upper_mask = hsv_img[:, :, 0] < 15
    mask1 = upper_mask * lower_mask

    lower_mask = hsv_img[:, :, 0] > 150
    upper_mask = hsv_img[:, :, 0] < 180
    mask2 = upper_mask * lower_mask

    mask = mask1 + mask2
    mask = mask.reshape(mask.shape + (1,))

    mask_3_channels = np.repeat(mask, 3, axis=2)
    res = img * mask_3_channels
    return res


def segment(img, hsv_img, hue_lower_limit, hue_upper_limit):
    lower_mask = hsv_img[:, :, 0] > hue_lower_limit
    upper_mask = hsv_img[:, :, 0] < hue_upper_limit
    saturation_mask = hsv_img[:, :, 1] > 0.3

    mask = upper_mask * lower_mask * saturation_mask
    mask = mask.reshape(mask.shape + (1,))

    mask_3_channels = np.repeat(mask, 3, axis=2)

    res = img * mask_3_channels
    return res


def segment_rgby(img, hsv_img):
    color = 'red'
    segmented_img = segment_red(img=img, hsv_img=hsv_img)
    cv.imshow(f"Segmented {color.capitalize()} Image", segmented_img)
    cv.waitKey(0)

    rgb_hue_segments = [(40, 80, 'green'), (80, 150, 'blue'), (15, 40, 'yellow')]
    for lower_limit, upper_limit, color in rgb_hue_segments:
        segmented_img = segment(img=img, hsv_img=hsv_img, hue_lower_limit=lower_limit, hue_upper_limit=upper_limit)

        cv.imshow(f"Segmented {color.capitalize()} Image", segmented_img)
        cv.waitKey(0)


def segment_all(img, hsv_img, skip=10):
    for lower in range(0, 300, skip):
        segmented_img = segment(img=img, hsv_img=hsv_img, hue_lower_limit=lower, hue_upper_limit=lower + skip)
        cv.imshow(f"Segmented {lower}-{lower+skip} Image", segmented_img)
        cv.waitKey(0)


IMAGE_PATH = "Res/objects.jpg"

img = cv.imread(IMAGE_PATH)

img = cv.resize(img, dsize=(img.shape[1] // 4, img.shape[0] // 4))

cv.imshow('Input', img)
cv.waitKey(0)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
cv.waitKey(0)


# compute_histogram(hsv)


# print("Displaying Segmentations based on histogram")

#hue_segments = [(0, 25), (75, 105), (105, 130)]

# hue_segments = [(0, 16), (16, 40), (100, 125)]

#for lower_limit, upper_limit in hue_segments:
#    segmented_img = segment(img=img, hsv_img=hsv, hue_lower_limit=lower_limit, hue_upper_limit=upper_limit)
#    cv.imshow("Segmented Image", segmented_img)
#    cv.waitKey(0)

segment_rgby(img=img, hsv_img=hsv)

cv.destroyAllWindows()
