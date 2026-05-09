from pathlib import Path
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


def load_preview_image(file_path, max_size=(420, 380)):
    """
    Load an image and resize it for GUI preview.
    This does not change the original image file.
    """
    image = Image.open(file_path)
    image = image.convert("RGB")
    image.thumbnail(max_size, Image.LANCZOS)
    return image


def get_filename(file_path):
    """
    Return only the filename from a full file path.
    """
    return Path(file_path).name