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
__date__ = '7/2/16' '6:44 PM'

class Imread_lesson:

    # define constructor
    def __init__(self, path):
        self.Image = path
        return

    # read image and display it
    def DisplayIt(self):
        # read image
        im = cv2.imread(self.Image)

        # print image information
        print("Width: %d pixels" % im.shape[1])
        print("Height: %d pixels" % im.shape[0])
        print("Channels: %d" % im.shape[2])

        # show image and wait for key press
        cv2.imshow("Image", im)
        cv2.waitKey(0)

