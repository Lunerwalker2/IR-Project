import numpy as np

class HorizontalSlice:
    def __init__(self, pt1, pt2, img):
        self.pt1 = pt1
        self.pt2 = pt2

        self.gray_image = img[pt1[1]:pt2[1], pt1[0]:pt2[0]]
        self.edge_image = np.zeros(np.shape(self.gray_image))
        self.color_image = np.zeros(self.gray_image.shape + (3,))

        self.vertical_average_list = []
        self.edge_x_locations = []
        self.center_point_locations = []
        self.center_point_colors = []

        self.fire_detected = False
        self.fire_edges = ()

        self.slice_id = -1
