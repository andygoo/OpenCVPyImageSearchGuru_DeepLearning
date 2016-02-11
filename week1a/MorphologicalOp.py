# These are my hobby project codes developed in python using OpenCV.
# Some of the projects are tested on Mac, Some on Raspberry Pi
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#



__author__ = 'kishwarkumar'
__date__ = '11/2/16' '7:53 PM'

# import the necessary packages
import numpy as np
import cv2

class MorphologicalOp:

    # define constructor
    def __init__(self, path):
        self.Image = path
        return

    # erosion
    def ErodeOp(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray image", gray)

        # apply a series of erosions
        for i in xrange(3):
            eroded = cv2.erode(gray.copy(), None, iterations=i+1)
            cv2.imshow("Erroded {} times".format(i+1), eroded)
            cv2.waitKey(0)

    # dilation
    def DiluteOp(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray image", gray)

        # apply a series of dilations
        for i in xrange(0, 3):
            dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
            cv2.imshow("Dilated {} times".format(i + 1), dilated)
            cv2.waitKey(0)

    # Opening
    def OpenOp(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray image", gray)

        kernelSizes = [(3,3), (5,5), (7,7)]
        # loop over the kernels and apply an "opening" operation on image
        for kernelSize in kernelSizes:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
            opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
            cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
            cv2.waitKey(0)

    # closing
    def ClosingOp(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray image", gray)

        kernelSizes = [(3,3), (5,5), (7,7)]
        # loop over the kernels and apply a "closing" operation to the image
        for kernelSize in kernelSizes:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
            closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
            cv2.imshow("Closing: ({}, {})".format(kernelSize[0], kernelSize[1]), closing)
            cv2.waitKey(0)

    # gradient
    def Gradient(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray image", gray)

        kernelSizes = [(3,3), (5,5), (7,7)]
        # loop over the kernels and apply a "morphological gradient" operation
        # to the image
        for kernelSize in kernelSizes:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
            gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
            cv2.imshow("Gradient: ({}, {})".format(kernelSize[0], kernelSize[1]), gradient)
            cv2.waitKey(0)

    # WhiteHat
    def WhiteHat(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray image", gray)

        # construct a rectangular kernel and apply a blackhat operation which
        # enables us to find dark regions on a light background
        rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
        blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

        # similarly, a tophat (also called a "whitehat") operation will enable
        # us to find light regions on a dark background
        tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

        # show the output images
        cv2.imshow("Original", im)
        cv2.imshow("Blackhat", blackhat)
        cv2.imshow("Tophat", tophat)
        cv2.waitKey(0)