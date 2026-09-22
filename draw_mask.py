import cv2
import numpy as np

image = cv2.imread("photo.png")

if image is None:
    raise FileNotFoundError("photo.png not found")

# Black mask = keep everything
mask = np.zeros(image.shape[:2], dtype=np.uint8)

drawing = False
brush_size = 20


def draw(event, x, y, flags, param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(mask, (x, y), brush_size, 255, -1)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.circle(mask, (x, y), brush_size, 255, -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(mask, (x, y), brush_size, 255, -1)


cv2.namedWindow("Draw Mask")
cv2.setMouseCallback("Draw Mask", draw)

while True:

    display = image.copy()

    # Show the masked area as white
    display[mask > 0] = [255, 255, 255]

    cv2.imshow("Draw Mask", display)

    key = cv2.waitKey(1) & 0xFF

    # Press S to save
    if key == ord("s"):
        cv2.imwrite("mask.png", mask)
        print("Mask saved as mask.png")
        break

    # Press ESC to cancel
    elif key == 27:
        print("Cancelled")
        break

cv2.destroyAllWindows()