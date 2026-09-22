# LaMa Image Inpainting with ONNX Runtime

A computer vision implementation of image inpainting using a
pretrained LaMa model in ONNX format, executed with ONNX Runtime
and OpenCV.

## Overview

Image inpainting is the process of reconstructing missing or
unwanted regions of an image.

This project allows a user to:

1. Load an image
2. Create a binary mask
3. Mark an unwanted region
4. Run the pretrained LaMa ONNX model
5. Generate an inpainted image

## How It Works

Original Image

      ↓
      
Create Mask

      ↓
      
Preprocessing

      ↓
      
LaMa ONNX Model

      ↓
      
Post-processing

      ↓
      
Inpainted Image

## Example

### Original
[image]

### Mask
[image]

### Result
[image]

## Technologies

- Python
- OpenCV
- NumPy
- ONNX
- ONNX Runtime
- LaMa

## Installation

...

## Usage

...

## Model

This project uses a pretrained LaMa model provided through
OpenCV Zoo.

The model itself is not included in this repository.

## Project Structure

...

## Learning Outcomes

Through this project, I worked with:

- Image preprocessing
- Binary masks
- ONNX model inspection
- Tensor dimensions
- Model inference
- Post-processing
- Computer vision workflows

## Acknowledgements

- OpenCV Zoo
- LaMa
