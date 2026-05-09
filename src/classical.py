import cv2


def upscale_bicubic(image, scale_factor=4):
    """
    Upscale image using Bicubic interpolation.
    """
    height, width = image.shape[:2]

    new_width = width * scale_factor
    new_height = height * scale_factor

    upscaled = cv2.resize(
        image,
        (new_width, new_height),
        interpolation=cv2.INTER_CUBIC
    )

    return upscaled


def upscale_lanczos(image, scale_factor=4):
    """
    Upscale image using Lanczos interpolation.
    """
    height, width = image.shape[:2]

    new_width = width * scale_factor
    new_height = height * scale_factor

    upscaled = cv2.resize(
        image,
        (new_width, new_height),
        interpolation=cv2.INTER_LANCZOS4
    )

    return upscaled


def apply_mild_sharpening(image):
    """
    Apply mild sharpening to improve edge clarity.
    """
    blurred = cv2.GaussianBlur(image, (0, 0), 1.0)

    sharpened = cv2.addWeighted(
        image,
        1.3,
        blurred,
        -0.3,
        0
    )

    return sharpened