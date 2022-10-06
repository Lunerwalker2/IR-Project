import cv2
import numpy as np

#Part A
# #creating an empty canvas | Remember zero pixel = black
img = np.zeros((512, 512, 3), np.uint8)
#
# #Draw horizontal line accross with thickness X
# #line(image, starting point, ending point, color, thickness)
# cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 7)
#
# #Display Image
# cv2.imshow("Image Window", img)
#
# #Waitkey to not close the window
# key = cv2.waitKey(0)

#Draw rectangle
cv2.rectangle( img, (384, 0), (510, 128), (0, 255, 0), 5 )

#Draw filled rectangle
cv2.rectangle( img, (0, 284), (120, 300), (0, 255, 0), -1 )

#Display Image
cv2.imshow( "Image Window", img )

#Waitkey to not close the window
key = cv2.waitKey(0)

# #Draw circle (img, center, radius, color)
# cv2.circle( img, (255, 255), 50, (0, 0, 255), 5 )
#
# #Display Image
# cv2.imshow( "Image Window", img )
#
# #Waitkey to not close the window
# key = cv2.waitKey(0)
#
# #Draw Ellipse (img, center, axes, angle, startangle, stopangle, color, thickness)
# cv2.ellipse( img, (255, 255), (100, 50), 0, 0, 180, (255, 255, 255), 7 )
#
# #Display Image
# cv2.imshow( "Image Window", img )
#
# #Waitkey to not close the window
# key = cv2.waitKey(0)
#
# #Draw Polygon
# points = np.array( [ [10, 5], [20, 30], [70, 20], [50, 10], [10, 5] ] )
# print(points)
# points.reshape( (-1, 1, 2) )
# print(points)
#
# #Draw Polygon from point array
# cv2.polylines( img, [points], True, (0, 255, 255) )
#
# #Display Image
# cv2.imshow( "Image Window", img )
#
# #Waitkey to not close the window
# key = cv2.waitKey(0)
#
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText( img, "Hello OpenCV", (10,100), font, 1, (255, 255, 255), 3, cv2.LINE_AA)
#
# #Display Image
# cv2.imshow( "Image Window", img )
#
# #Waitkey to not close the window
# key = cv2.waitKey(0)

#----------------------------------------------------#

#OpenCV is BGR by default not RGB
#Part B - Manipulating individual pixels
# img = cv2.imread( 'messi5.jpg' )

# #Display Image
# cv2.imshow( "Image Messi", img )

# #Waitkey to not close the window
# key = cv2.waitKey(0)

# print('image shape:', img.shape )

# #Access Single Pixel
# pixel = img[255, 255]
# print('pixel at 255, 255:', pixel )

# #just blue color
# pixel_blue = img[255, 255, 0]
# print('blue color at 255, 250:', pixel_blue )

# #change single pixel
# img[255, 255] = [255, 255, 255]

# print('pixel at 255, 255:', img[255, 255] )

# #just blue color
# pixel_red = img[30, 30, 2]
# print('Red color at pixel 30, 30:', pixel_red )

# #modify red value
# img.itemset( (30, 30, 2), 100 )
# print('image item at 30, 30:', img.item( 30, 30, 2) )

# #Display Image
# cv2.imshow( "Image Messi", img )

# #Waitkey to not close the window
# key = cv2.waitKey(0)

#-----------------------------------------------------------#
#Part C

# # Read image
# img = cv2.imread('ml.png')
# print('image shape', img.shape)
# img_logo = cv2.imread('opencv-logo.png')
#
# print('Image Shape:', img.shape)
# print('Logo Shape:', img_logo.shape)
#
# width = img.shape[1]
# height = img.shape[0]
#
# img_logo = cv2.resize(img_logo,
#                       (width,
#                        height),
#                        interpolation = cv2.INTER_AREA)
# combined = cv2.addWeighted(img, 0.7, img_logo, 0.3, 0.0)
#
# print('Combined Shape:', Combined.shape)
#
# cv2.imshow('combined', combined)
#
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()

#-----------------------------------------------------------#
# #Part D - Displaying and saving image using s
# import sys

# img = cv2.imread( cv2.samples.findFile("starry_night.jpg") )

# if img is None:
#     sys.exit("Could not read the image.")

# #print total number of elements
# print('Image Size:', img.size )
# #print the shape of the array row,col,z
# print('Image Shape:', img.shape )

# #Display Image
# cv2.imshow( "Image Starry Night", img )

# #Waitkey to not close the window
# key = cv2.waitKey(0)

# #ord returns the ASCII/Unicode integer value of the input
# if( key == ord('s') ):
#     cv2.imwrite('starry_save.png', img)

# area_of_interest = img[10:131, 10:131]

# #replace section with area of interest    
# img[100:221, 100:221] = area_of_interest

# print('Share of area of interest', area_of_interest.shape)

# #Display Image
# cv2.imshow( "Image Area of Interest Replace", img )

# #Waitkey to not close the window
# key = cv2.waitKey(0)

# #changing color scheme

# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #Display Image
# cv2.imshow( "Gray Image", gray_img )

# #Waitkey to not close the window
# key = cv2.waitKey(0)

# import_gray_img = cv2.imread( 'starry_night.jpg', cv2.IMREAD_GRAYSCALE )

# #Display Image
# cv2.imshow( "Gray Image", import_gray_img )

# #Waitkey to not close the window
# key = cv2.waitKey(0)

#------------------------------------------------------#
# #Part E - Image Capture From Camera
# capture = cv2.VideoCapture( 0 )

# if not capture.isOpened():
#     print( 'cannot open the camera device' )
#     exit()

# while True:
#     ret, frame = capture.read()

#     if not ret:
#         print( 'cannot capture a frame' )
#         continue

#     gray_frame = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )

#     #Display Image
#     cv2.imshow( "Gray Image", gray_frame )

#     #Waitkey to not close the window
#     key = cv2.waitKey(0)

#     #close video capture with q
#     if key == ord( 'q' ):
#         break

# capture.release()
# cv2.destroyAllWindows()

#-----------------------------------------------------------#
# # Part F - Print options in CV2

# options = [ i for i in dir(cv2) if i.startswith( 'COLOR_' ) ]
# print( options )

#-----------------------------------------------------------#
# Part G - Saving Video Files or Frames, Opening Video File As Capture
# #open video file
# capture = cv2.VideoCapture("IMG_6826.MOV")
# #Capture from camera deviec
# capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# #set 3 - width, 4 - height, 5 -fps ,etc. VideoCapture.set
# capture.set(3,340)
# capture.set(4,340)

# # Define the codec and create VideoWriter object
# #fourcc = cv.VideoWriter_fourcc(*'XVID')
# #out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
# #Save as MP4 - common web video format
# # fourcc = cv2.VideoWriter_fourcc(*'MP4V')
# # out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))
# while capture.isOpened():
#     ret, frame = capture.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # frame = cv2.flip(frame, 0)
#     # Save single frame
#     #out.write(frame)
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
# # Release everything if job is finished
# capture.release()
# cv2.destroyAllWindows()

#------------------------------------------------------------#
# Part H - tracking colored objects
# capture = cv2.VideoCapture(0)
# capture.set(3,350)
# capture.set(4,350)

# while True:
#     ret, frame = capture.read()

#     #convert BGR to HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # define range of blue color in HSV
#     lower_blue = np.array( [110,50,50] ) 
#     upper_blue = np.array( [130,255,255] )
#     #lower_red = np.array( [0, 100, 100] )
#     #upper_red = np.array( [10, 255, 255] )

#     # Threshold the HSV image to get only blue colors
#     mask_obj = cv2.inRange(hsv, lower_blue, upper_blue)

#     #bitwise and mask on original frame
#     result = cv2.bitwise_and(frame, frame, mask = mask_obj)

#     cv2.imshow('Original Frame', frame)
#     cv2.imshow('Mask', mask_obj)
#     cv2.imshow('Masked Result', result)

#     lower_blue_new = np.array( [100,40,40] ) 
#     upper_blue_new = np.array( [140,255,255] )
#     mask_new = cv2.inRange(hsv, lower_blue_new, upper_blue_new)
#     result_new = cv2.bitwise_and(frame, frame, mask = mask_new)
#     cv2.imshow('Result With New Mask',result_new)

#     key = cv2.waitKey(1) & 0xFF 
#     '''
#         cv2.waitKey(1) returns the character code of the currently 
#         pressed key and -1 if no key is pressed. The & 0xFF is a 
#         binary AND operation to ensure only the single byte (ASCII) 
#         representation of the key remains as for some operating systems.
#         cv2.waitKey(1) will return a code that is not a single byte. 
#         ord('q') always returns the ASCII representation of 'q' 
#         which is 113 (0x71 in hex).
#      '''
#     if key == ord( 'q' ):
#         break

# cv2.destroyAllWindows()

#-----------------------------------------------------------#
# Part I - Canny Edge Detection

# # read in the image as gray or convert using cv2.cvtColor()
# img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE) 

# #Display Image
# cv2.imshow( "Gray Image", img )

# #Waitkey to not close the window
# key = cv2.waitKey(0)

# #canny using image and lower and upper thresholds
# edges_1 = cv2.Canny(img, 100, 200)

# #Display Image
# cv2.imshow( "Edges 1 Image", edges_1 )

# #Waitkey to not close the window
# key = cv2.waitKey(0)

# #canny using image and lower and upper thresholds
# edges_2 = cv2.Canny(img, 200, 230)

# #Display Image
# cv2.imshow( "Edges 2 Image", edges_2 )

# #Waitkey to not close the window
# key = cv2.waitKey(0)

# #canny using image and lower and upper thresholds
# edges_3 = cv2.Canny(img, 230, 250)

# #Display Image
# cv2.imshow( "Edges 3 Image", edges_3 )

# #Waitkey to not close the window
# key = cv2.waitKey(0)

#-----------------------------------------------------------#
# Part J - Template Matching

# # # read in the image as gray or convert using cv2.cvtColor()
# img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)

# #create copy
# img_copy = img.copy()

# #open template
# template = cv2.imread('messi_face.jpg', cv2.IMREAD_GRAYSCALE)

# cv2.imshow(  "Orginal Image", img )
# cv2.imshow("Template", template )
# cv2.waitKey(0)

# # All the 6 methods for comparison in a list
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# width, height = template.shape[::-1]

# for method in methods:
#     img = img_copy.copy()
#     method_eval = eval( method )

#     # Apply template Matching
#     result = cv2.matchTemplate(img, template, method_eval)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#     # threshold = 0.8
#     # loc = np.where( result >= threshold)
#     # for pt in zip(*loc[::-1]):
#     #     cv2.rectangle(img, pt, (pt[0] + width, pt[1] + height), (0,0,255), 2)

#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method_eval in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc

#     bottom_right = (top_left[0] + width, top_left[1] + height)
#     cv2.rectangle(img, top_left, bottom_right, 255, 2)    #mark the face on the image

#     cv2.imshow("Matched Result", img)
#     cv2.waitKey(0)

#-----------------------------------------------------------#
# Part K - Feature Matching Sift model

# #number of features to match
# MIN_MATCH_COUNT = 10
# #read in original image
# img = cv2.imread( 'box_in_scene.png' )
# #read in query image
# img_query = cv2.imread('box_3.png') # query image
# #if no image return
# if img_query is None:
#     print('Query Image Does Not Exist')
#     exit()

# #Show Images
# cv2.imshow("object", img_query)
# cv2.imshow("scene image",img)

# key = cv2.waitKey(0)

# #detect the feature, SIFT detector, Scale-Invariant Feature Transform
# sift = cv2.SIFT_create()

# # find the keypoints and descriptors with SIFT
# kp1, des1 = sift.detectAndCompute(img_query, None)
# kp2, des2 = sift.detectAndCompute(img, None)

# #Algorithm Selection
# FLANN_INDEX_KDTREE = 1
# #get index parameters as dictionary
# index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
# #get search parameters
# search_params = dict(checks = 50)
# #Use flann based matcher
# flann = cv2.FlannBasedMatcher( index_params, search_params )
# #get KNN matches for K value of 2
# matches = flann.knnMatch(des1, des2, k=2)
# # store all the good matches as per Lowe's ratio test.
# good = []
# for m, n in matches:
#     if m.distance < 0.7  *n.distance:
#         good.append( m )

# if len(good) > MIN_MATCH_COUNT:
#     #Get source and destination points and reshape array
#     src_pts = np.float32( [ kp1[m.queryIdx].pt for m in good ] ).reshape(-1,1,2)
#     dst_pts = np.float32( [ kp2[m.trainIdx].pt for m in good ] ).reshape(-1,1,2)
#     #find homography on source/destination points
#     M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

#     #matched mast to list
#     matchesMask = mask.ravel().tolist()
#     #get height width and depth
#     h,w,d = img_query.shape

#     #reshape points array to match height width
#     pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)

#     dst = cv2.perspectiveTransform(pts,M)
#     #draw lines and set color
#     img_polylines = cv2.polylines(img, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

#     #show polylines
#     cv2.imshow("matching image",img_polylines)

#     key = cv2.waitKey(0)

#     # draw matches in green color
#     draw_params = dict(matchColor = (0, 255, 0), 
#                    singlePointColor = None,
#                    matchesMask = matchesMask, # draw only inliers
#                    flags = 2)

#     #Get Matched Image using drawMatches
#     img_matched = cv2.drawMatches( img_query, kp1, img, kp2, good, None, **draw_params )
#     #display matched features
#     cv2.imshow( "Matched Feature Items", img_matched )
#     #pause windows until close
#     key = cv2.waitKey(0)

#------------------------------------------------------------#
# Part L - Video Match
MIN_MATCH_COUNT = 10

capture = cv2.VideoCapture("IMG_6826.MOV")
img_book = cv2.imread('Book.png')
capture.set(3,340)
capture.set(4,340)

# Initiate SIFT detector
sift = cv2.SIFT_create()
# find the keypoints and descriptors with SIFT in target image
kp1, des1 = sift.detectAndCompute(img_book, None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

while capture.isOpened():
    e1 = cv2.getTickCount()
    ret, frame = capture.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow('Original Frame', frame)

    kp2, des2 = sift.detectAndCompute(frame, None)
    matches = flann.knnMatch(des1, des2, k=2)
    good = []
    for m,n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32( [ kp1[m.queryIdx].pt for m in good ] ).reshape(-1,1,2)
        dst_pts = np.float32( [ kp2[m.trainIdx].pt for m in good ] ).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()
        h,w,d = img_book.shape

        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)
        img_polylines = cv2.polylines(frame,[np.int32(dst)],True,255,3, cv2.LINE_AA)

        cv2.imshow('Detected Features', img_polylines)
    else:
        print( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
        matchesMask = None

    # your code execution
    e2 = cv2.getTickCount()
    time = (e2 - e1)/ cv2.getTickFrequency()
    print("takes: ", time)

    if cv2.waitKey(5) >= 0:
        break
# Release everything if job is finished
capture.release()
cv2.destroyAllWindows()


