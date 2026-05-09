from pathlib import Path
import cv2
from PIL import Image


SUPPORTED_IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff",
    ".webp",
}


def is_supported_image(file_path):
    """
    Check whether the selected file is a supported image format.
    """
    return Path(file_path).suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS


def load_cv_image(file_path):
    """
    Load an image using OpenCV.
    """
    image = cv2.imread(file_path)

    if image is None:
        raise ValueError("Could not read image file.")

    return image


def cv_to_pil(image):
    """
    Convert OpenCV BGR image to PIL RGB image.
    """
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb_image)


def load_preview_image(file_path, max_size=(420, 380)):
    """
    Load an image and resize it for GUI preview.
    This does not change the original image file.
    """
    image = Image.open(file_path)
    image = image.convert("RGB")
    image.thumbnail(max_size, Image.LANCZOS)
    return image


def create_preview_from_cv(image, max_size=(420, 380)):
    """
    Create a resized PIL preview image from an OpenCV image.
    """
    preview_image = cv_to_pil(image)
    preview_image.thumbnail(max_size, Image.LANCZOS)
    return preview_image


def get_filename(file_path):
    """
    Return only the filename from a full file path.
    """
    return Path(file_path).name


def get_scale_factor(scale_text):
    """
    Convert scale text such as '2x' or '4x' into integer scale factor.
    """
    return int(scale_text.replace("x", ""))