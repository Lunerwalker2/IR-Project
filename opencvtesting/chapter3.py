import cv2
import  numpy as np

img = cv2.imread("Resources/robot2.jpg")
print(img.shape)

imgResize = cv2.resize(img, (900, 600))
print(imgResize.shape)

imgCropped = imgResize[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)



cv2.waitKey(0)
