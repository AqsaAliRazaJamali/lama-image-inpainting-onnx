import cv2
import numpy as np

# Read the original image
image = cv2.imread("photo.png")

# Get the dimesnsions of image
height, width = image.shape[:2]

# Create a completely black mask
mask = np.zeros((height, width), dtype=np.uint8)

# Create a white rectangle in the center
x1 = width // 3
y1 = height // 3
x2 = 2 * width // 3
y2 = 2 * height // 3

mask[y1:y2, x1:x2] = 255

# Save the mask
cv2.imwrite("mask.png", mask)

print("Mask created successfully!")
print("Image size:", width, "x", height)
