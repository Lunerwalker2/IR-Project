import cv2
import numpy as np
from horizontal_slice import HorizontalSlice


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

        region = HorizontalSlice(pt1, pt2, normalized_img)
        # Section off the region to add
        horizontal_scans.append(region)
        last_y_pos += distance_between_lines

    return horizontal_scans


def find_smoke_edges(slice_list):
    # Go through each slice and find the edges
    for region in slice_list:
        region.edge_image = cv2.Canny(region.gray_image, 80, 200, L2gradient=True)


# Throw out strips with no edges in them
def prune_edges(slice_list):
    # New list
    pruned_list = []

    length = len(slice_list)
    # Check the mean of each region to see if its above 0
    for x in range(length):
        mean = np.average(slice_list[x].edge_image)
        if mean != 0.0:
            pruned_list.append(slice_list[x])

    return pruned_list


# Average the vertical columns of gray pixels into a 1D array of values for each slice
def average_columns(slice_list):
    for region in slice_list:
        columns = np.hsplit(region.gray_image, region.gray_image.shape[1])
        for column in columns:
            # Use the first element of the 4 channel scalar for gray
            average_value = cv2.mean(column)[0]
            region.vertical_average_list.append(average_value)


def find_edges(slice_list):
    for region in slice_list:
        last_result_black = False
        for x in range(len(region.vertical_average_list)):
            print(region.vertical_average_list[x])
            if region.vertical_average_list[x] > 200:
                if last_result_black: region.edge_x_locations.append(x)
                last_result_black = False
            elif region.vertical_average_list[x] < 50:
                if not last_result_black: region.edge_x_locations.append(x)
                last_result_black = True
