class HorizontalSlice:
    def __init__(self, pt1, pt2, img):
        self.pt1 = pt1
        self.pt2 = pt2

        self.region = img[pt1[1]:pt2[1], pt1[0]:pt2[0]]


