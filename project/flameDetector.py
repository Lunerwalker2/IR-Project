import cv2
import numpy as np

# read the image and convert to hsv
img = cv2.imread('images/forestfire.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display original image
cv2.imshow("OG Image", img)

# covers the red-yellow range of a flame
lower_flame = np.array([0, 128, 128])
upper_flame = np.array([25, 255, 255])

# Create a mask object with the limits
flame_mask = cv2.inRange(img_hsv, lower_flame, upper_flame)

# Apply mask to original image
img_masked = cv2.bitwise_and(img, img, mask=flame_mask)

# Display mask
cv2.imshow("Mask", flame_mask)
# Display the masked image
cv2.imshow("Masked Image", img_masked)

# Waitkey to not close the window
key = cv2.waitKey(0)
