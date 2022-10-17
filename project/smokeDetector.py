import cv2
import numpy as np


def show_image(name, mat):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, mat)


def normalizeImage(image, offset, ROI_point, ROI_size):
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


# Specify erode and dilate elements
erodeElement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilateElement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# Read image and convert to grayscale
img = cv2.imread('images/forestfire3.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



# Specify an ROI in the frame (middle 50% horizontally)
x, y = 0, int(0.25 * img_gray.shape[0])
w, h = img_gray.shape[1], int(0.5 * img_gray.shape[0])
# ROI = img_gray[x:x + w, y:y + h]

img_morph = normalizeImage(img_gray, 0.75, (x, y), (w, h))

# Blur the image
cv2.GaussianBlur(img_morph, (5, 5), 0, dst=img_morph)

img_noised = cv2.fastNlMeansDenoising(img_morph, None, 10, 7, 21)

cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
cv2.rectangle(img_gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

show_image('Original Image', img)
show_image('Grayed/Blurred Image', img_gray)
show_image('Morphed Image', img_morph)
show_image('Denoised Image', img_noised)

cv2.waitKey(0)
