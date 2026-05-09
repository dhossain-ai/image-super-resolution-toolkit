from pathlib import Path

import cv2


def upscale_edsr(image, scale_factor=4, model_dir="models"):
    """
    Upscale an image using a pretrained EDSR model.

    The model file must be placed inside the models folder.
    Example:
        models/EDSR_x4.pb
    """
    if scale_factor != 4:
        raise ValueError("EDSR currently supports only 4x scale in this app.")

    if not hasattr(cv2, "dnn_superres"):
        raise RuntimeError(
            "OpenCV dnn_superres module not found. "
            "Install opencv-contrib-python instead of opencv-python."
        )

    model_path = Path(model_dir) / "EDSR_x4.pb"

    if not model_path.exists():
        raise FileNotFoundError(
            f"EDSR model file not found: {model_path}\n\n"
            "Please download the pretrained EDSR_x4.pb model and place it inside the models folder."
        )

    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(str(model_path))
    sr.setModel("edsr", scale_factor)

    upscaled = sr.upsample(image)

    return upscaled