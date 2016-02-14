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
__date__ = '13/2/16' '10:38 PM'

class Gradient:

    # define constructor
    def __init__(self, path):
        self.Image = path
        return

    # Sobel
    def Gradient_Sobel(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # compute gradients along the X and Y axis, respectively
        gX = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
        gY = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)

        # the `gX` and `gY` images are now of the floating point data type,
        # so we need to take care to convert them back to an unsigned 8-bit
        # integer representation so other OpenCV functions can utilize them
        gX = cv2.convertScaleAbs(gX)
        gY = cv2.convertScaleAbs(gY)

        # combine the sobel X and Y representations into a single image
        sobelCombined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

        # show our output images
        cv2.imshow("Sobel X", gX)
        cv2.imshow("Sobel Y", gY)
        cv2.imshow("Sobel Combined", sobelCombined)
        cv2.waitKey(0)