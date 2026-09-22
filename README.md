# Image Inpainting with LaMa and ONNX Runtime

A Python-based computer vision project that performs **image inpainting** using a pretrained **LaMa model in ONNX format**.

The project allows an unwanted object or region in an image to be selected using a mask. The LaMa model then reconstructs that region using the surrounding visual information.

The implementation uses **OpenCV**, **NumPy**, and **ONNX Runtime** to prepare the image and mask, run model inference, and save the resulting image.

> **Note:** LaMa is a pretrained model used by this project. The LaMa model itself was not developed or trained from scratch.

---

## Overview

Image inpainting is the process of removing unwanted or missing parts of an image and filling the selected area with a visually plausible reconstruction.

For example, suppose an image contains an unwanted object:

```text
Original Image

+-------------------------------+
|                               |
|       Background              |
|                               |
|          [OBJECT]             |
|                               |
|       Background              |
|                               |
+-------------------------------+
```

We create a mask over the object:

```text
Mask

+-------------------------------+
|                               |
|       Black                   |
|                               |
|          [WHITE]              |
|                               |
|       Black                   |
|                               |
+-------------------------------+
```

In this project:

- **Black = keep the original area**
- **White = remove and reconstruct the area**

The image and mask are then passed to the LaMa model.

The model attempts to generate a natural-looking replacement for the masked region.

---

## How It Works

The complete process is:

```text
Original Image
      |
      v
Create Mask
      |
      v
Preprocess Image + Mask
      |
      v
LaMa ONNX Model
      |
      v
ONNX Runtime Inference
      |
      v
Post-process Model Output
      |
      v
Save Inpainted Image
```

The important idea is that the model receives **both the image and the mask**.

The image tells the model what the scene looks like.

The mask tells the model:

> "This is the region that needs to be reconstructed."

---

## Features

- Image inpainting using a pretrained LaMa model
- ONNX model inference
- Local processing using ONNX Runtime
- Interactive mask drawing
- Programmatic mask creation
- ONNX model input/output inspection
- OpenCV-based image processing
- Supports removing selected objects or regions
- No external image-processing API is required for inference

---

## Technologies

- Python
- OpenCV
- NumPy
- ONNX
- ONNX Runtime
- LaMa
- Computer Vision
- Deep Learning

---

## Project Structure

```text
lama-image-inpainting-onnx/
│
├── README.md
├── inpaint.py
├── draw_mask.py
├── create_mask.py
├── inspect_model.py
├── requirements.txt
├── .gitignore
│
└── models/
    └── inpainting_lama_2025jan.onnx
```

### Files

| File | Purpose |
|---|---|
| `README.md` | Complete project documentation |
| `inpaint.py` | Runs image inpainting using the ONNX model |
| `draw_mask.py` | Allows the user to draw a mask interactively |
| `create_mask.py` | Creates a mask programmatically |
| `inspect_model.py` | Displays the ONNX model's inputs and outputs |
| `requirements.txt` | Contains the required Python packages |
| `.gitignore` | Prevents unnecessary files and the large model from being committed |

---

# Requirements

Before running the project, make sure you have:

- Python 3.10 or newer
- pip
- OpenCV
- NumPy
- ONNX Runtime
- The pretrained LaMa ONNX model

The project was developed and tested using Python on Windows.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/AqsaAliRazaJamali/lama-image-inpainting-onnx.git
```

Move into the project directory:

```bash
cd lama-image-inpainting-onnx
```

---

## 2. Create a Virtual Environment

Creating a virtual environment keeps the project's dependencies separate from other Python projects.

On Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

The project's dependencies are:

```text
numpy
opencv-python
onnxruntime
```

---

# Model Setup

The project uses a pretrained LaMa model in ONNX format.

The model is **not committed to GitHub** because the model file is approximately 92 MB and is unnecessary to store directly in the source repository.

Download the required ONNX model and place it in:

```text
models/
└── inpainting_lama_2025jan.onnx
```

The expected project structure is therefore:

```text
lama-image-inpainting-onnx/
│
├── README.md
├── inpaint.py
├── draw_mask.py
├── create_mask.py
├── inspect_model.py
├── requirements.txt
├── .gitignore
│
└── models/
    └── inpainting_lama_2025jan.onnx
```

Make sure the model path used in `inpaint.py` matches this location.

---

# Preparing the Input Image

Place the image you want to process in the project directory.

For example:

```text
photo.png
```

The image should contain the object or region that you want to remove.

For example:

```text
Project Folder
│
├── photo.png
├── inpaint.py
└── ...
```

---

# Creating the Mask

A mask is used to tell the model which part of the image should be reconstructed.

The project includes an interactive mask-drawing program.

Run:

```bash
python draw_mask.py
```

A window will open displaying the image.

Use the mouse to paint over the object you want to remove.

Press:

```text
S
```

to save the mask.

The mask will be saved as:

```text
mask.png
```

---

## Mask Rules

The mask uses two basic values:

```text
Black (0)   = Preserve
White (255) = Inpaint
```

Therefore, if an object is on the left side of the image, the white region of the mask must cover that object.

For example:

```text
Original:

+--------------------------------+
|                                |
|  ########                      |
|  ########       Background     |
|  ########                      |
|                                |
+--------------------------------+
```

The corresponding mask should be:

```text
Mask:

+--------------------------------+
|                                |
|  ████████                      |
|  ████████       Black          |
|  ████████                      |
|                                |
+--------------------------------+
```

The white region tells LaMa which area should be reconstructed.

### Important

The mask should cover the **entire unwanted object**.

If part of the object is outside the mask, the model is not instructed to remove that part.

At the same time, making the mask unnecessarily large can remove surrounding information that the model could have used for reconstruction.

---

# Running the Inpainting

After creating `mask.png`, run:

```bash
python inpaint.py
```

The program performs the following operations:

1. Loads the original image.
2. Loads the mask.
3. Resizes the image and mask to the model's required dimensions.
4. Converts the image and mask into the required numerical format.
5. Creates the model inputs.
6. Loads the pretrained LaMa ONNX model.
7. Runs inference using ONNX Runtime.
8. Processes the model output.
9. Saves the final inpainted image.

The resulting image is saved by `inpaint.py` according to its configured output filename.

---

# Inspecting the ONNX Model

Before running inference, the model can be inspected using:

```bash
python inspect_model.py
```

This script displays the model's input and output information.

The model used by this project expects:

```text
INPUT: image
Shape: [batch, 3, 512, 512]
Type: tensor(float)

INPUT: mask
Shape: [batch, 1, 512, 512]
Type: tensor(float)

OUTPUT: output
Shape: [batch, 3, 512, 512]
Type: tensor(float)
```

Understanding these dimensions is important because the input data must match the format expected by the neural network.

---

# Understanding the Model Input

## Image Input

The image input has the shape:

```text
[batch, 3, 512, 512]
```

The four values represent:

```text
batch
channels
height
width
```

So:

```text
[1, 3, 512, 512]
```

means:

- `1` → one image
- `3` → three color channels
- `512` → image height
- `512` → image width

The three channels represent the RGB color information.

---

## Mask Input

The mask has the shape:

```text
[1, 1, 512, 512]
```

The mask has only one channel because it is a single grayscale mask.

Therefore:

```text
Image:
[1, 3, 512, 512]

Mask:
[1, 1, 512, 512]
```

The image contains three color channels, while the mask only needs one channel.

---

# Why Preprocessing Is Necessary

A PNG or JPEG image is not automatically in the format required by a neural network.

For example, OpenCV normally represents an image using a height-width-channel arrangement.

The model expects:

```text
Batch × Channels × Height × Width
```

Therefore, the program must transform the image before sending it to the model.

The general process is:

```text
Image File
    |
    v
Open with OpenCV
    |
    v
Resize
    |
    v
Convert image format
    |
    v
Convert to floating point
    |
    v
Rearrange dimensions
    |
    v
Model Input
```

The mask goes through a similar preprocessing process.

This is one of the important practical parts of working with pretrained models:

> A pretrained model still requires its input to be prepared in exactly the format it expects.

---

# Model Inference

Once the image and mask have been prepared, they are passed to ONNX Runtime.

Conceptually:

```text
Image Tensor
     +
Mask Tensor
     |
     v
ONNX Runtime
     |
     v
LaMa Model
     |
     v
Output Tensor
```

The model analyzes the surrounding image information and generates a reconstructed version of the masked region.

---

# Post-processing

The neural network produces numerical output.

This output must be converted back into an image that can be displayed or saved.

The general process is:

```text
Model Output
     |
     v
Convert output array
     |
     v
Convert to image format
     |
     v
Save as PNG/JPEG
```

---

# Complete Technical Pipeline

```text
                  Original Image
                        |
                        v
                ┌───────────────┐
                │    OpenCV     │
                │ Image Loading │
                └───────┬───────┘
                        |
                        v
                 Image Preprocessing
                        |
                        |
Mask ─────────► Mask Preprocessing
                        |
                        v
                ┌───────────────┐
                │  Image Tensor │
                │       +       │
                │  Mask Tensor  │
                └───────┬───────┘
                        |
                        v
                ┌───────────────┐
                │  LaMa ONNX    │
                │     Model     │
                └───────┬───────┘
                        |
                        v
                  ONNX Runtime
                    Inference
                        |
                        v
                  Model Output
                        |
                        v
                 Post-processing
                        |
                        v
                Inpainted Image
```

---

# Example Workflow

A safe example can be stored in:

```text
examples/
├── original.png
├── mask.png
└── inpainted.png
```

### `original.png`

The original image containing the unwanted object.

### `mask.png`

The mask showing the region that should be reconstructed.

### `inpainted.png`

The final image produced by the LaMa model.

The three files demonstrate:

```text
Original
   ↓
Mask
   ↓
Inpainted Result
```

Example images are optional. The project does not require them to run.

---

# Important: Personal Images

Do **not** upload a personal or private image to GitHub simply for the purpose of demonstrating the project.

For example, if `photo.png` is a private photograph, keep it locally:

```text
photo.png
mask.png
inpainted.png
```

and do not commit those files.

For the GitHub repository, use a safe image that:

- You created yourself, or
- You own, or
- Has a license allowing redistribution.

The same applies to images containing other people's personal information.

---

# What Should Be Uploaded to GitHub?

The following project files should be included:

```text
README.md
inpaint.py
draw_mask.py
create_mask.py
inspect_model.py
requirements.txt
.gitignore
```

A safe example can optionally be included:

```text
examples/
├── original.png
├── mask.png
└── inpainted.png
```

---

# What Should NOT Be Uploaded?

Avoid committing:

```text
.venv/
__pycache__/
*.pyc
```

Do not upload:

```text
models/inpainting_lama_2025jan.onnx
```

if you are intentionally keeping the large model outside the repository.

Also do not upload:

- Private photographs
- Sensitive images
- Personal data
- Unrelated files
- Large temporary files
- IDE-specific files that are not required by the project

---

# `.gitignore`

A suitable `.gitignore` for this project is:

```gitignore
# Virtual environment
.venv/

# Python cache
__pycache__/
*.pyc

# ONNX model
models/*.onnx

# IDE files
.vscode/
.idea/

# Local input/output images
photo.png
mask.png
inpainted.png
```

This prevents local files and the large ONNX model from accidentally being committed.

---

# Requirements File

The `requirements.txt` file should contain:

```text
numpy
opencv-python
onnxruntime
```

Install them with:

```bash
pip install -r requirements.txt
```

---

# Learning Outcomes

This project provided practical experience with:

### Computer Vision

Understanding how images can be manipulated and reconstructed programmatically.

### Image Inpainting

Understanding how unwanted image regions can be reconstructed using surrounding information.

### Image Masks

Understanding how masks are used to identify regions that should be modified.

### Pretrained Models

Learning how an existing trained model can be integrated into an application instead of building and training a model from scratch.

### ONNX

Understanding how a machine-learning model can be represented in the ONNX format.

### ONNX Runtime

Learning how to execute an ONNX model locally.

### Tensor Shapes

Understanding why a model might expect data such as:

```text
[1, 3, 512, 512]
```

instead of a normal image representation.

### Model Inspection

Learning how to inspect a model before implementing inference code.

### OpenCV

Practicing:

- Reading images
- Writing images
- Resizing images
- Creating masks
- Drawing masks
- Processing image arrays

### Debugging

The project also involved debugging practical problems such as:

- Invalid image files
- Incorrect masks
- Incorrect mask placement
- Model input shapes
- Output scaling
- Image preprocessing
- Model output processing

---

# Limitations

The final result depends on several factors.

## Mask Accuracy

The mask must correctly cover the unwanted object.

A mask that is too small may leave parts of the object visible.

A mask that is too large may remove useful surrounding information.

## Background Complexity

Simple backgrounds can be easier to reconstruct than highly detailed backgrounds.

## Large Missing Regions

Very large masked regions may be more difficult to reconstruct because less surrounding information is available.

## Model Limitations

The final result depends on the capabilities of the pretrained LaMa model.

The model does not know exactly what was originally behind the removed object. It generates a plausible reconstruction based on the available image context.

---

# Future Improvements

Possible future improvements include:

- Add a graphical user interface
- Add drag-and-drop image support
- Add adjustable brush size
- Add an eraser
- Add undo and redo
- Add before/after preview
- Add automatic object detection
- Generate masks automatically
- Support batch image processing
- Add more image formats
- Improve error handling
- Add progress indicators
- Add side-by-side result comparison

---

# Privacy

The project is designed to perform the model inference locally.

Users should still avoid exposing private images or sensitive information.

For a public GitHub repository:

- Use safe example images.
- Do not upload private photographs.
- Do not upload images containing sensitive information.
- Do not upload someone else's personal photograph without permission.
- Do not commit local input images accidentally.

---

# Acknowledgements

This project uses a **pretrained LaMa image-inpainting model**.

The LaMa model was not developed or trained from scratch as part of this project.

The purpose of this project is to understand how a pretrained computer-vision model can be integrated into a practical Python application using:

```text
Python
   +
OpenCV
   +
NumPy
   +
ONNX Runtime
   +
Pretrained LaMa
```

---

# License

This repository contains the project source code, utilities, and documentation.

The pretrained model and any third-party assets may have their own licenses and usage requirements.

Please review the applicable licenses before redistributing the pretrained model or third-party resources.

---

# Author

**Aqsa Ali Raza Jamali**

Computer Science Student  
Sukkur IBA University

---

# Project Summary

This project demonstrates a complete image-inpainting workflow using a pretrained LaMa model.

The process is:

```text
Input Image
     |
     v
Create Mask
     |
     v
Preprocess Image + Mask
     |
     v
LaMa ONNX Model
     |
     v
ONNX Runtime Inference
     |
     v
Post-process Output
     |
     v
Inpainted Image
```

The project focuses on practical understanding of:

**Computer Vision → Image Inpainting → Masking → Pretrained Models → ONNX → ONNX Runtime → OpenCV → Neural Network Inference**
