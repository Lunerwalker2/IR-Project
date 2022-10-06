import cv2
import numpy as np

# Part H - tracking colored objects

capture = cv2.VideoCapture(1)
capture.set(3, 350)
capture.set(4, 350)

while True:
    ret, frame = capture.read()

    #convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array( [110,50,50] )
    upper_blue = np.array( [130,255,255] )
    #lower_red = np.array( [0, 100, 100] )
    #upper_red = np.array( [10, 255, 255] )

    # Threshold the HSV image to get only blue colors
    mask_obj = cv2.inRange(hsv, lower_blue, upper_blue)

    #bitwise and mask on original frame
    result = cv2.bitwise_and(frame, frame, mask = mask_obj)

    cv2.imshow('Original Frame', frame)
    cv2.imshow('Mask', mask_obj)
    cv2.imshow('Masked Result', result)

    lower_blue_new = np.array( [100,40,40] )
    upper_blue_new = np.array( [140,255,255] )
    mask_new = cv2.inRange(hsv, lower_blue_new, upper_blue_new)
    result_new = cv2.bitwise_and(frame, frame, mask = mask_new)
    cv2.imshow('Result With New Mask',result_new)

    key = cv2.waitKey(1) & 0xFF
    '''
        cv2.waitKey(1) returns the character code of the currently 
        pressed key and -1 if no key is pressed. The & 0xFF is a 
        binary AND operation to ensure only the single byte (ASCII) 
        representation of the key remains as for some operating systems.
        cv2.waitKey(1) will return a code that is not a single byte. 
        ord('q') always returns the ASCII representation of 'q' 
        which is 113 (0x71 in hex).
     '''
    if key == ord( 'q' ):
        break

cv2.destroyAllWindows()
