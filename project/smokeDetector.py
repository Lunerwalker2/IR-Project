import cv2
import numpy as np

# Specify erode and dilate elements
erodeElement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilateElement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# Read image and convert to grayscale
img = cv2.imread('images/forestfire4.jpeg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image
# cv2.GaussianBlur(img_gray, (7, 7), 0, dst=img_gray)

# Specify an ROI in the frame (set in stone for now)
x, y = 450, 120
w, h = 200, 220
ROI = img_gray[y:y+h, x:x+h]


# Find mean and STD
mean, STD = cv2.meanStdDev(ROI)

# Use an offset value to scale how much is clipped
offset = 0.75

# Clip the image to the range of the STD in the ROI
img_clipped = np.clip(img_gray, mean - offset*STD, mean + offset*STD).astype(np.uint8)

# Normalize whole image from the clipped result
img_norm = cv2.normalize(img_clipped, img_clipped, 0, 255, norm_type=cv2.NORM_MINMAX)

# Erode and dilate image slightly to get rid of things like trees
img_morph = cv2.erode(img_norm, erodeElement, iterations=2)
img_morph = cv2.dilate(img_morph, dilateElement, iterations=2)

cv2.rectangle(img_gray, (x, y), (x+w, y+h), (0, 255, 0))

cv2.imshow("Original Image", img)
cv2.imshow('Original Gray Image', img_gray)
cv2.imshow('ROI', ROI)
cv2.imshow('Normalized Image', img_norm)
cv2.imshow("Morphed Image", img_morph)
cv2.waitKey(0)





