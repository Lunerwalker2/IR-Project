import cv2
import numpy as np
from cv2.mat_wrapper import Mat

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
roi_x, roi_y = 0, int(0.25 * img_gray.shape[0])
w, h = img_gray.shape[1], int(0.5 * img_gray.shape[0])

# Normalize the image
img_morph = smoke_detector.normalize_image(img_gray, 0.75, (roi_x, roi_y), (w, h))

# De-noise the image
img_noised = smoke_detector.denoise(img_morph)

######
# Scanning
# Just based on difference between smoke and none smoke for now

# Get a list of the sliced mats of the image to go over
list_of_regions = smoke_scanner.split_into_lines(img_noised, 7, 13)

# # Show all the regions
# for x in range(len(list_of_regions)):
#     show_image(f"Region {x}", list_of_regions[x].gray_image, False)

# Find edges in the slices
smoke_scanner.find_smoke_edges(list_of_regions)

# Show all the edges
# for x in range(len(list_of_regions)):
#     show_image(f"Edges {x}", list_of_regions[x].edge_image, False)

# Remove slices without edges
list_of_regions = smoke_scanner.prune_edges(list_of_regions)

# Show the slices with edges
# for x in range(len(list_of_regions)):
#     show_image(f"Only With Edges {x}", list_of_regions[x].edge_image, False)

# Store the color version of the slices
img_color_blurred = smoke_detector.denoise_color(img)

for x in range(len(list_of_regions)):
    region = list_of_regions[x]
    # print(region.color_image.shape)
    region.color_image = img_color_blurred[region.pt1[1]:region.pt2[1], region.pt1[0]:region.pt2[0]]
    # print(region.color_image.shape)

# Show the slices with edges
# for x in range(len(list_of_regions)):
#     show_image(f"Recolorized slices {x}", list_of_regions[x].color_image, False)

smoke_scanner.average_columns(list_of_regions)

smoke_scanner.find_edges(list_of_regions)

# Toss out any slices without edges
for x in range(len(list_of_regions)):
    locations = list_of_regions[x].edge_x_locations
    if len(locations) == 1 and locations[0] == 0:
        list_of_regions.pop(x)
        x += 1

# Draw the lines on the slices and show them
# for x in range(len(list_of_regions)):
#     # print(region.edge_x_locations)
#     copy = list_of_regions[x].color_image.copy()
#     for y in range(len(list_of_regions[x].edge_x_locations)):
#         cv2.line(copy, (list_of_regions[x].edge_x_locations[y], 0),
#                  (list_of_regions[x].edge_x_locations[y], list_of_regions[x].pt2[1]), (10, 250, 10), 4)
#     show_image(f"edges drawn {x}", copy, False)

# Find the RGB color of each centerpoint
smoke_scanner.sample_middle(list_of_regions)

# Show the color images
# for x in range(len(list_of_regions)):
#     print(list_of_regions[x].center_point_colors)

# show_image(f"cb of {x}", list_of_regions[x].color_image, False)


############

not_sky_list = list_of_regions.copy()

# Knock out any slices with significant blue that isn't just plain smoke i.e. sky
for x in range(len(list_of_regions)):
    region = list_of_regions[x]

    take_out = False

    previous_white = False
    previous_other = False

    # convert to hsl and do smth ig
    for y in range(len(region.center_point_colors)):
        hsl_color = smoke_scanner.bgr_to_hsl(region.center_point_colors[y])
        hsl_color = hsl_color.round(3)

        # if blue
        if 200 < hsl_color[0] < 240:

            # If it's a strong blue, assume sky
            if hsl_color[1] > 0.7:
                print("blue", hsl_color, x)
                take_out = True
                break
            # Smoke??????
            if hsl_color[2] > 0.6:
                print("smoke????", hsl_color, x)

                # DING DING DING DING DING DING DING DING
                if previous_other:
                    not_sky_list[x].slice_id = x
                    not_sky_list[x].fire_detected = True
                    not_sky_list[x].fire_edges = (
                        region.center_point_locations[y - 1], region.center_point_locations[y]
                    )
                    break

                # Mark the smoke for now
                previous_white = True
                previous_other = False

        if 0 <= hsl_color[0] <= 200 or hsl_color[0] >= 240:
            print("other", hsl_color, x)
            # DING DING DING DING DING DING DING DING
            if previous_white:
                not_sky_list[x].slice_id = x
                not_sky_list[x].fire_detected = True
                not_sky_list[x].fire_edges = (
                    region.center_point_locations[y - 1], region.center_point_locations[y]
                )
                break

            previous_other = True
            previous_white = False

    if take_out:
        not_sky_list.pop(x)

# for x in range(len(not_sky_list)):
#     show_image(f"new thing {x}", not_sky_list[x].color_image, False)

# Check for fires
for region in not_sky_list:
    if region.fire_detected:
        print("DING DING DING DING DING DING")

        print(region.pt1, region.pt2, region.fire_edges, region.slice_id)
        cv2.rectangle(img,
                      (region.fire_edges[0], region.pt1[1] - 145),
                      (region.fire_edges[1], region.pt2[1] - 145),
                      (0, 0, 255),
                      3
                      )

        # show_image("FIRE FIRE FIRE FIRE FIRE FIRE FIRE FIRE", img, False)
        break

#


######

# Draw a rectangle to indicate the ROI area
# cv2.rectangle(img, (roi_x, roi_y), (roi_x + w, roi_y + h), (0, 0, 0), 2)
# cv2.rectangle(img_gray, (roi_x, roi_y), (roi_x + w, roi_y + h), (0, 255, 0), 4)

show_image('Original Image', img)
# show_image('Contrast Image', cv2.multiply(img, (1.2, 1.2, 1.2, 1.2)))
# show_image('Grayed/Blurred Image', img_gray)
# show_image('Morphed Image', img_morph)
# show_image('De-Noised Image', img_noised)

cv2.waitKey(0)
