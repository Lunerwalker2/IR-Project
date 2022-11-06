import cv2
import numpy as np

erodeElement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilateElement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))


def normalize_image(image, offset, ROI_point, ROI_size):
    """
    Normalizes the given grayscale image using the specified ROI and offset value.
    """
    x, y = ROI_point
    w, h = ROI_size

    # Specify the region of interest in the frame
    ROI = image[x:x + w, y:y + h]

    # Find mean and STD
    mean, STD = cv2.meanStdDev(ROI)

    # Clip the image to the range of the STD in the ROI
    img_clipped = np.clip(image, mean - offset * STD, mean + offset * STD).astype(np.uint8)

    # Normalize whole image from the clipped result
    img_norm = cv2.normalize(img_clipped, img_clipped, 0, 255, norm_type=cv2.NORM_MINMAX)

    # Erode and dilate image slightly to get rid of things like trees
    img_morph = cv2.erode(img_norm, erodeElement, iterations=2)
    img_morph = cv2.dilate(img_morph, dilateElement, iterations=2)

    return img_morph


def denoise(image):
    # Blur the image
    img_blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # de-noise the image to wipe out any random bits of stuff
    return cv2.fastNlMeansDenoising(img_blurred, None, 12, 7, 21)


def denoise_color(image):
    # Blur the image
    img_blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # de-noise the image to wipe out any random bits of stuff
    # return cv2.fastNlMeansDenoisingColored(img_blurred, None, 10, 7, 20)
    return img_blurred