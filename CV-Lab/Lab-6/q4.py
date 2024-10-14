import cv2
import imutils

ORIGINAL_SHAPE = None

def load_images(image_path):
    global ORIGINAL_SHAPE
    images = []
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found: {image_path}")
    height, width, ch = img.shape
    ORIGINAL_SHAPE = img.shape
    img1 = img[:int(height * .75), :int(width * .8), :]
    img2 = img[int(height * .35):, int(width * .5):, :]
    img2 = imutils.rotate(img2, 30)
    images.append(img1)
    images.append(img2)

    cv2.imshow("Image 1", img1)
    cv2.imshow("Image 2", img2)
    cv2.waitKey(0)

    return images

def stitch_images(images):
    # Initialize the stitcher
    stitcher = cv2.Stitcher_create()

    # Perform stitching
    status, stitched = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        print("Stitching completed successfully.")
        return stitched
    else:
        print("Error during stitching.")
        return None


# List of image paths to stitch (adjust these paths)
image_path = 'Res/people.webp'

# Load images
images = load_images(image_path)

# Stitch images
stitched_image = stitch_images(images)

stitched_image = cv2.resize(stitched_image, (stitched_image.shape[1] // 5, stitched_image.shape[0]))

# Show the result
if stitched_image is not None:
    cv2.imshow('Stitched Image', stitched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


