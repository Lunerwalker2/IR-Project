import cv2
import numpy as np
import smoke_detector
import smoke_scanner


def show_image(name, mat, resize=True):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL) if resize else cv2.namedWindow(name)
    cv2.imshow(name, mat)


######
# SMOKE

# Read image and convert to grayscale
img = cv2.imread('images/forestfire3.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Specify an ROI in the frame (middle 50% horizontally)
x, y = 0, int(0.25 * img_gray.shape[0])
w, h = img_gray.shape[1], int(0.5 * img_gray.shape[0])

# Normalize the image
img_morph = smoke_detector.normalize_image(img_gray, 0.75, (x, y), (w, h))

# De-noise the image
img_noised = smoke_detector.denoise(img_morph)

# Draw a rectangle to indicate the ROI area
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
cv2.rectangle(img_gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

######
# Scanning
# Just based on difference between smoke and none smoke for now

# Get a list of the sliced mats of the image to go over
list_of_regions = smoke_scanner.split_into_lines(img_noised, 5, 11)

# Show all the regions
for x in range(len(list_of_regions)):
    show_image(f"Region {x}", list_of_regions[x], False)

######

# show_image('Original Image', img)
# show_image('Grayed/Blurred Image', img_gray)
# show_image('Morphed Image', img_morph)
show_image('De-Noised Image', img_noised)

cv2.waitKey(0)
