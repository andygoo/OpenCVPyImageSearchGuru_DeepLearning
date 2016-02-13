# These are my hobby project codes developed in python using OpenCV.
# Some of the projects are tested on Mac, Some on Raspberry Pi
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

# imports
import cv2
from skimage.filter import threshold_adaptive

__author__ = 'kishwarkumar'
__date__ = '13/2/16' '8:15 PM'

class Thresholding:

    # define constructor
    def __init__(self, path):
        self.Image = path
        return

    # Simple Thresholding
    def Simple_Thresholding(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        cv2.imshow("Image", im)

        # apply basic thresholding -- the first parameter is the image
        # we want to threshold, the second value is our threshold check
        # if a pixel value is greater than our threshold (in this case,
        # 200), we set it to be BLACK, otherwise it is WHITE.
        (T, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
        cv2.imshow("Threshold Binary Inverse", threshInv)

        # using normal thresholding (rather than inverse thresholding),
        # we can change the last argument in the function to make the coins
        # black rather than white.
        (T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
        cv2.imshow("Threshold Binary", thresh)

        # finally, we can visualize only the masked regions in the image
        cv2.imshow("Output", cv2.bitwise_and(im, im, mask=threshInv))
        cv2.waitKey(0)


    # Otsu Thresholding
    def Otsu_Thresholding(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        cv2.imshow("Image", im)

        # apply Otsu's automatic thresholding -- Otsu's method automatically
        # determines the best threshold value `T` for us
        (T, threshInv) = cv2.threshold(blurred, 0, 255,
	        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        cv2.imshow("Threshold", threshInv)
        print "Otsu's thresholding value: {}".format(T)

        # finally, we can visualize only the masked regions in the image
        cv2.imshow("Output", cv2.bitwise_and(im, im, mask=threshInv))
        cv2.waitKey(0)

    # Adaptive Thresholding
    def Adaptive_Thresholding(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        cv2.imshow("Image", im)

        # instead of manually specifying the threshold value, we can use adaptive
        # thresholding to examine neighborhoods of pixels and adaptively threshold
        # each neighborhood -- in this example, we'll calculate the mean value
        # of the neighborhood area of 25 pixels and threshold based on that value;
        # finally, our constant C is subtracted from the mean calculation (in this
        # case 15)
        thresh = cv2.adaptiveThreshold(blurred, 255,
            cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15)
        cv2.imshow("OpenCV Mean Thresh", thresh)

        # personally, I prefer the scikit-image adaptive thresholding, it just
        # feels a lot more "Pythonic"
        thresh = threshold_adaptive(blurred, 30, offset=5).astype("uint8") * 255
        thresh = cv2.bitwise_not(thresh)
        cv2.imshow("scikit-image Mean Thresh", thresh)
        cv2.waitKey(0)