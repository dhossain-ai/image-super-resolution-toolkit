# Super-Resolution Comparison App

A Python Tkinter application for comparing image super-resolution methods, including classical interpolation techniques and pretrained EDSR deep learning upscaling.

## Features

- Select a low-resolution image
- Apply classical upscaling methods:
  - Bicubic interpolation
  - Lanczos interpolation
- Apply deep learning super-resolution:
  - EDSR pretrained model
- Preview original and enhanced images
- Save enhanced output images locally

## Methods

### Classical Super-Resolution

The app supports Bicubic and Lanczos interpolation using OpenCV.

### Deep Learning Super-Resolution

The app supports EDSR using OpenCV's `dnn_superres` module with a pretrained `.pb` model.

## Project Structure

```text
super-resolution-comparison-app/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── models/
├── input/
├── output/
├── screenshots/
└── src/
    ├── classical.py
    ├── deep_learning.py
    ├── image_utils.py
    └── gui.py