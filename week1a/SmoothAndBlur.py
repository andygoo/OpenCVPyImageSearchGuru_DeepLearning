# These are my hobby project codes developed in python using OpenCV.
# Some of the projects are tested on Mac, Some on Raspberry Pi
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

# imports
import cv2

__author__ = 'kishwarkumar'
__date__ = '11/2/16' '8:49 PM'

class SmoothNBlur:

    # define constructor
    def __init__(self, path):
        self.Image = path
        return

    # Blur by averaging
    def BlurAvg(self):
        # read image
        im = cv2.imread(self.Image)
        cv2.imshow("Original image", im)

        kernelSizes = [(3, 3), (9, 9), (15, 15)]
        # loop over the kernel sizes and apply an "average" blur to the image
        for (kX, kY) in kernelSizes:
            blurred = cv2.blur(im, (kX, kY))
            cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
            cv2.waitKey(0)

    # Blur by gaussian
    def Blurgaus(self):
        # read image
        im = cv2.imread(self.Image)
        cv2.imshow("Original image", im)

        kernelSizes = [(3, 3), (9, 9), (15, 15)]
        # loop over the kernel sizes and apply an "gaussian" blur to the image
        for (kX, kY) in kernelSizes:
            blurred = cv2.GaussianBlur(im, (kX, kY), 0)
            cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
            cv2.waitKey(0)

    # Blur by median
    def Blurmed(self):
        # read image
        im = cv2.imread(self.Image)
        cv2.imshow("Original image", im)

        # loop over the kernel sizes and apply an "median" blur to the image
        for k in (3, 9, 15):
            blurred = cv2.medianBlur(im, k)
            cv2.imshow("Gaussian ({})".format(k), blurred)
            cv2.waitKey(0)

    # Blur by bilateral
    def Blurbil(self):
        # read image
        im = cv2.imread(self.Image)
        cv2.imshow("Original image", im)

        params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
        # loop over the diameter, sigma color, and sigma space
        for (diameter, sigmaColor, sigmaSpace) in params:
            # apply bilateral filtering and display the image
            blurred = cv2.bilateralFilter(im, diameter, sigmaColor, sigmaSpace)
            title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
            cv2.imshow(title, blurred)
            cv2.waitKey(0)