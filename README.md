# 🖼️ Image Inpainting with LaMa and ONNX Runtime

A computer vision project that uses a **pretrained LaMa (Large Mask Inpainting) model** in **ONNX format** to remove unwanted objects or regions from images and reconstruct the missing areas.

The project uses **Python, OpenCV, NumPy, and ONNX Runtime** to create masks, preprocess images, run the pretrained model, and generate the final inpainted image.

> **Important:** This project integrates and uses a pretrained LaMa model. The LaMa model architecture was not developed or trained from scratch as part of this project.

---

## 📖 Table of Contents

- [Overview](#-overview)
- [What is Image Inpainting?](#-what-is-image-inpainting)
- [How the Project Works](#-how-the-project-works)
- [Project Workflow](#-project-workflow)
- [Technologies Used](#-technologies-used)
- [Model Information](#-model-information)
- [Model Inputs and Outputs](#-model-inputs-and-outputs)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Model Setup](#-model-setup)
- [Usage](#-usage)
- [Creating a Mask](#-creating-a-mask)
- [Running Inpainting](#-running-inpainting)
- [Inspecting the ONNX Model](#-inspecting-the-onnx-model)
- [Understanding the Mask](#-understanding-the-mask)
- [Understanding Tensor Shapes](#-understanding-tensor-shapes)
- [Technical Pipeline](#-technical-pipeline)
- [Example](#-example)
- [What I Learned](#-what-i-learned)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Privacy](#-privacy)
- [Acknowledgements](#-acknowledgements)
- [License](#-license)
- [Author](#-author)

---

# 📌 Overview

Image inpainting is a **computer vision technique** used to remove unwanted regions from an image and reconstruct those regions using information from the surrounding area.

For example, an image may contain:

- An unwanted object
- A person in the background
- Text or a watermark
- Scratches
- Damaged regions
- Other objects that need to be removed

Instead of simply deleting the selected pixels, an inpainting model tries to **generate a visually reasonable replacement** for the missing region.

This project demonstrates how a pretrained **LaMa image-inpainting model** can be integrated into a Python application using **ONNX Runtime**.

The project also includes an interactive tool for creating masks with the mouse.

---

# 🧠 What is Image Inpainting?

Imagine you have this image:

```text
┌───────────────────────────────┐
│                               │
│        Background             │
│                               │
│             █████             │
│             █████             │
│             █████             │
│                               │
└───────────────────────────────┘
