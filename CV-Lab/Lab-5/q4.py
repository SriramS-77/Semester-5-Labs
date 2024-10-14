import cv2
import numpy as np
import matplotlib.pyplot as plt


def extract_hog_features(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Set HOG parameters
    hog = cv2.HOGDescriptor()

    # Compute HOG features
    hog_features = hog.compute(gray_image)

    return hog_features, image


def visualize_hog(image, hog_features):
    # Display the image and HOG features
    plt.figure(figsize=(12, 6))

    # Display original image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')

    # Display HOG features
    plt.subplot(1, 2, 2)
    plt.plot(hog_features, color='blue')
    plt.title("HOG Features")
    plt.xlabel("HOG Feature Index")
    plt.ylabel("Value")

    plt.tight_layout()
    plt.show()


# Path to your image
image_path = 'Res/people.webp'  # Change to your image path

# Load the image
image = cv2.imread(image_path)
if image is None:
    print(f"Error loading image: {image_path}")

else:
    # Extract HOG features
    hog_features, resized_image = extract_hog_features(image)

    # Visualize HOG features
    visualize_hog(resized_image, hog_features)
