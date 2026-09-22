# 🖼️ Image Inpainting with LaMa and ONNX Runtime

An image inpainting project that uses a **pretrained LaMa (Large Mask Inpainting) model** in **ONNX format** to remove unwanted objects or regions from images and intelligently fill the missing area.

The project uses **OpenCV** for image and mask processing and **ONNX Runtime** for running the pretrained deep-learning model locally.

> **Note:** This project uses a pretrained LaMa model. The LaMa architecture itself was not developed from scratch.

---

## ✨ Overview

Image inpainting is the process of **removing unwanted parts of an image and reconstructing the missing region** so that it looks natural.

For example, if an image contains:

- an unwanted object
- a person or object in the background
- text or a watermark
- scratches or damaged regions

we can mark that area with a **mask**, and the inpainting model attempts to reconstruct what could naturally appear there.

This project provides a simple workflow:

```text
Original Image
      ↓
Create / Provide Mask
      ↓
Preprocess Image + Mask
      ↓
LaMa ONNX Model
      ↓
Post-process Output
      ↓
Inpainted Image
