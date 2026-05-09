# Super-Resolution Comparison App

A Python Tkinter desktop application for comparing classical and deep learning image super-resolution methods.

The app supports low-resolution image enhancement using:

- Bicubic interpolation
- Lanczos interpolation
- EDSR deep learning super-resolution
- Optional post-processing:
  - Denoising
  - Sharpening
  - Contrast enhancement

This project runs locally and does not use online APIs or cloud services.

---

## Features

- Select an input image from your computer
- Choose a super-resolution method
- Choose scale factor: 2x or 4x
- Preview original and enhanced images
- Apply optional post-processing
- Save the enhanced output image locally
- Compare classical interpolation with deep learning super-resolution

---

## Methods Used

### 1. Bicubic Interpolation

Bicubic interpolation is a classical image resizing method. It estimates new pixel values using nearby pixels and produces smoother results than nearest-neighbor or bilinear interpolation.

### 2. Lanczos Interpolation

Lanczos interpolation is another classical upscaling method. It often preserves edges better than bicubic interpolation and is useful for images with lines, borders, and structured objects.

### 3. EDSR

EDSR stands for Enhanced Deep Super-Resolution Network. It is a deep learning model designed to reconstruct high-resolution images from low-resolution inputs.

In this project, EDSR is used through OpenCV's `dnn_superres` module with a pretrained `.pb` model file.

---

## Project Structure

```text
super-resolution-comparison-app/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── EDSR_x4.pb
│
├── input/
├── output/
├── screenshots/
│
└── src/
    ├── __init__.py
    ├── classical.py
    ├── deep_learning.py
    ├── image_utils.py
    └── gui.py
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/image-super-resolution-toolkit.git
cd image-super-resolution-toolkit
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## EDSR Model Setup

To use the EDSR method, place the pretrained model file inside the `models/` folder.

Required file:

```text
models/EDSR_x4.pb
```

The filename must be exactly:

```text
EDSR_x4.pb
```

If the model file is missing, Bicubic and Lanczos will still work, but EDSR will show an error.

---

## Run the App

```bash
python app.py
```

---

## How to Use

1. Open the application.
2. Click **Select Image**.
3. Choose a low-resolution image.
4. Select a method:
   - Bicubic
   - Lanczos
   - EDSR
5. Select a scale factor:
   - 2x
   - 4x
6. Choose optional post-processing:
   - Denoising
   - Sharpening
   - Contrast
7. Click **Process Image**.
8. Preview the output image.
9. Click **Save Output** to save the result in the `output/` folder.

---

## Notes

- EDSR currently supports only 4x scaling in this app.
- Bicubic and Lanczos support both 2x and 4x scaling.
- Output images are saved as `.png` files.
- This project does not use cloud APIs or online image enhancement services.

---

## Example Output Filename

```text
output/input_image_lanczos_4x.png
```

If a file with the same name already exists, the app automatically adds a timestamp.

---

## Technologies Used

- Python
- Tkinter
- OpenCV
- Pillow
- NumPy

---

## Assignment Context

This project was developed for an image super-resolution task. The objective is to increase the resolution of a low-resolution historical image while restoring visual details using both classical interpolation and deep learning-based methods.

---

## License

This project is for academic and educational use.
