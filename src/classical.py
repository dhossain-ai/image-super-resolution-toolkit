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


def apply_mild_denoising(image):
    """
    Apply mild denoising to reduce noise while preserving details.
    """
    denoised = cv2.fastNlMeansDenoisingColored(
        image,
        None,
        h=3,
        hColor=3,
        templateWindowSize=7,
        searchWindowSize=21
    )

    return denoised


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


def apply_contrast_enhancement(image):
    """
    Apply mild contrast and brightness enhancement.
    """
    enhanced = cv2.convertScaleAbs(
        image,
        alpha=1.08,
        beta=3
    )

    return enhanced


def apply_post_processing(
    image,
    use_denoising=True,
    use_sharpening=True,
    use_contrast=True
):
    """
    Apply selected post-processing steps.
    """
    processed = image.copy()

    if use_denoising:
        processed = apply_mild_denoising(processed)

    if use_sharpening:
        processed = apply_mild_sharpening(processed)

    if use_contrast:
        processed = apply_contrast_enhancement(processed)

    return processed