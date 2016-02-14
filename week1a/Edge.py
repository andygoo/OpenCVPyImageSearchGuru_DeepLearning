# These are my hobby project codes developed in python using OpenCV.
# Some of the projects are tested on Mac, Some on Raspberry Pi
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

# imports
import cv2
import imutils

__author__ = 'kishwarkumar'
__date__ = '13/2/16' '11:00 PM'

class Edge:

    # define constructor
    def __init__(self, path):
        self.Image = path
        return

    # Edge detection using Canny
    def Edge_Canny(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # show the original and blurred images
        cv2.imshow("Original", im)
        cv2.imshow("Blurred", blurred)

        # compute a "wide", "mid-range", and "tight" threshold for the edges
        wide = cv2.Canny(blurred, 10, 200)
        mid = cv2.Canny(blurred, 30, 150)
        tight = cv2.Canny(blurred, 240, 250)

        # show the edge maps
        cv2.imshow("Wide Edge Map", wide)
        cv2.imshow("Mid Edge Map", mid)
        cv2.imshow("Tight Edge Map", tight)
        cv2.waitKey(0)

    # Edge detection using Canny (auto thresholding)
    def Edge_Canny_auto(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)

        # apply Canny edge detection using a wide threshold, tight
        # threshold, and automatically determined threshold
        wide = cv2.Canny(blurred, 10, 200)
        tight = cv2.Canny(blurred, 225, 250)
        auto = imutils.auto_canny(blurred)

        # show the images
        cv2.imshow("Original", im)
        cv2.imshow("Wide", wide)
        cv2.imshow("Tight", tight)
        cv2.imshow("Auto", auto)
        cv2.waitKey(0)