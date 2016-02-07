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

    # display upper left corner of the image
    def DisplayUpperLeft(self):
        # read image
        im = cv2.imread(self.Image)

        # get image centre
        (cX, cY) = (im.shape[1]/2, im.shape[0]/2)

        # as it is NumPy arrays, we can slicing
        tl = im[0:cY, 0:cX]
        cv2.imshow("Top-Left Corner", tl)
        cv2.waitKey(0)

    # display all corners
    def DisplayCorners(self):
        # read image
        im = cv2.imread(self.Image)

        # measure size
        (h, w) = im.shape[:2]

        # get image cetre
        (cX, cY) = (w/2, h/2)

        # as it is NumPy arrays, we can slicing
        tl = im[0:cY, 0:cX]
        tr = im[0:cY, cX:w]
        br = im[cY:h, cX:w]
        bl = im[cY:h, 0:cX]

        cv2.imshow("Top-Left Corner", tl)
        cv2.imshow("Top-Right Corner", tr)
        cv2.imshow("Bottom-Left Corner", bl)
        cv2.imshow("Bottom-Right Corner", br)

        cv2.waitKey(0)

    # lets make image tl green
    def image_tl_green(self):
        # read image
        im = cv2.imread(self.Image)

        # pixel information
        (b, g, r) = im[111, 225]
        print("red=%d, green=%d, blue=%d" % (r,g,b))
        print "Pixel at (111, 225) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)

        # measure size
        (h, w) = im.shape[:2]

        # get image cetre
        (cX, cY) = (w/2, h/2)

        # as it is NumPy arrays, we can slicing
        im[0:cY, 0:cX] = (0, 0, 255)

        # show image
        #cv2.imshow("updated", im)

        #wait for key
        #cv2.waitKey(0)