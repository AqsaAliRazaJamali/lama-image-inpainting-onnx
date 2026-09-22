import cv2
import numpy as np
import onnxruntime as ort

MODEL_PATH = "inpainting_lama_2025jan.onnx"
IMAGE_PATH = "photo.png"
MASK_PATH = "mask.png"
OUTPUT_PATH = "inpainted.png"

# Load image and mask
image = cv2.imread(IMAGE_PATH)
mask = cv2.imread(MASK_PATH, cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Could not find photo.png")

if mask is None:
    raise FileNotFoundError("Could not find mask.png")

# Keep the original dimensions
original_height, original_width = image.shape[:2]

# Resize to the model's required 512 x 512 input
image_512 = cv2.resize(image, (512, 512))
mask_512 = cv2.resize(
    mask,
    (512, 512),
    interpolation=cv2.INTER_NEAREST
)

# -----------------------------
# Prepare IMAGE
# -----------------------------

# Convert pixel values from 0-255 to 0-1
image_blob = image_512.astype(np.float32) / 255.0

# HWC -> CHW
image_blob = np.transpose(image_blob, (2, 0, 1))

# Add batch dimension
image_blob = np.expand_dims(image_blob, axis=0)

# -----------------------------
# Prepare MASK
# -----------------------------

# Convert mask to 0 or 1
mask_blob = (mask_512 > 0).astype(np.float32)

# Add channel dimension
mask_blob = np.expand_dims(mask_blob, axis=0)

# Add batch dimension
mask_blob = np.expand_dims(mask_blob, axis=0)

# -----------------------------
# Load ONNX model
# -----------------------------

session = ort.InferenceSession(MODEL_PATH)

# -----------------------------
# Run model
# -----------------------------

result = session.run(
    ["output"],
    {
        "image": image_blob,
        "mask": mask_blob
    }
)

# Get output for first image
output = result[0][0]

# CHW -> HWC
output = np.transpose(output, (1, 2, 0))

# The OpenCV LaMa model already produces 0-255 values.
# Convert directly to uint8.
output = np.clip(output, 0, 255).astype(np.uint8)

# -----------------------------
# Resize result back
# -----------------------------

output = cv2.resize(
    output,
    (original_width, original_height),
    interpolation=cv2.INTER_LINEAR
)

# -----------------------------
# Save
# -----------------------------

cv2.imwrite(OUTPUT_PATH, output)

print("Inpainting completed successfully!")
print("Output saved as:", OUTPUT_PATH)