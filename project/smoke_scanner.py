import cv2
import numpy as np
from horizontal_slice import HorizontalSlice
import math


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
    # print(distance_between_lines)

    # Create a list for the scanned regions
    horizontal_scans = []

    # print(normalized_img.shape)

    last_y_pos = 0
    # Fill with the y positions of each line
    for y in range(num_lines):
        # Top left corner
        pt1 = (0, last_y_pos)
        # print(pt1)

        # Bottom right corner
        # pt2 = (normalized_img.shape[1], int(last_y_pos + ((pixel_width - 1) / 2)))
        pt2 = (normalized_img.shape[1], last_y_pos + pixel_width)
        # print(pt2)

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


# Mark locations of sudden color change
def find_edges(slice_list):
    for region in slice_list:
        last_result_black = False

        for x in range(len(region.vertical_average_list)):
            # print(region.vertical_average_list[x])

            if region.vertical_average_list[x] > 200:
                if last_result_black: region.edge_x_locations.append(x)
                last_result_black = False

            elif region.vertical_average_list[x] < 50:
                if not last_result_black: region.edge_x_locations.append(x)
                last_result_black = True


# Give the average color of the center points in the colorized slice between edges
def sample_middle(slice_list):
    for region in slice_list:

        # If the first value isn't 0, add it
        if not region.edge_x_locations[0] == 0:
            region.edge_x_locations.insert(0, 0)

        # If the first value isn't the end of the frame, add it
        if not region.edge_x_locations[-1] == region.gray_image.shape[1]:
            region.edge_x_locations.append(region.gray_image.shape[1])

        # Find the colors at the center of each area marked by the edges
        for x in range(len(region.edge_x_locations) - 1):
            # Find the middle between two edges
            center_point = int((region.edge_x_locations[x] + region.edge_x_locations[x + 1]) / 2)

            # if x == 0:
            #     print(region.color_image.shape)
            # print(np.average(region.color_image[:, center_point], axis=0))

            # Convert to YCrCb
            # ycrcb_image = cv2.cvtColor(region.color_image, cv2.COLOR_BGR2YCrCb)

            # Average the color in that column and store it
            region.center_point_colors.append(np.average(region.color_image[:, center_point], axis=0))


def bgr_to_hsl(bgr_scalar):
    H, S, L = 0.0, 0.0, 0.0

    # Normalize to 0-1
    b = bgr_scalar[0]
    g = bgr_scalar[1]
    r = bgr_scalar[2]

    c_max = max(r, g, b)
    c_min = min(r, g, b)

    delta = (c_max - c_min) / 255

    L = (0.5 * (c_max + c_min)) / 255

    if L > 0.0:
        S = delta / (1 - abs((2 * L) - 1))
    else:
        S = 0.0

    top = r - (0.5 * g) - (0.5 * b)
    root = math.sqrt(math.pow(r, 2) + math.pow(g, 2) + math.pow(b, 2) - r * g - r * b - g * b)

    if g >= b:
        H = math.degrees(math.acos(top / root))
    else:
        H = 360 - math.degrees(math.acos(top / root))

    if math.isnan(H):
        H = 0

    return np.array((H, S, L))
