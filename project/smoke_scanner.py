import cv2
import numpy as np


# The basic idea is to have a few lines scanning through the image and try to find
# some edge between black and white (forest to smoke).

def split_into_lines(normalized_img, num_lines, pixel_width):
    """
    Return a list of the regions to scan
    """

    # Ensure the width is greater than 1 and an odd number
    assert pixel_width % 2 == 1 and pixel_width != 1

    total_height = normalized_img.shape[0]

    # Find the distance between each line
    distance_between_lines = int(total_height / num_lines)
    print(distance_between_lines)

    # Create a list for the scanned regions
    horizontal_scans = []

    print(normalized_img.shape)

    last_y_pos = 0
    # Fill with the y positions of each line
    for y in range(num_lines):

        # Top left corner
        pt1 = (0, last_y_pos)
        print(pt1)

        # Bottom right corner
        pt2 = (normalized_img.shape[1], int(last_y_pos + ((pixel_width - 1) / 2)))
        print(pt2)

        region = normalized_img[pt1[1]:pt2[1], pt1[0]:pt2[0]]
        # Section off the region to add
        horizontal_scans.append(region)
        last_y_pos += distance_between_lines

    return horizontal_scans

