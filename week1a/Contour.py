# These are my hobby project codes developed in python using OpenCV.
# Some of the projects are tested on Mac, Some on Raspberry Pi
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#

# imports
import cv2
import numpy as np

__author__ = 'kishwarkumar'
__date__ = '15/2/16' '8:29 PM'

class Contour:

    # define constructor
    def __init__(self, path):
        self.Image = path
        return

    # Contour Operations
    def ContourOp(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # find all contours in the image and draw ALL contours on the image
        (cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        clone = im.copy()
        # cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
        cv2.drawContours(clone, cnts[2], -1, (0, 255, 0), 1)
        print "Found {} contours".format(len(cnts))

        # show the output image
        cv2.imshow("All Contours", clone)
        cv2.waitKey(0)

        # re-clone the image and close all open windows
        clone = im.copy()
        cv2.destroyAllWindows()

        # loop over the contours individually and draw each of them
        for (i, c) in enumerate(cnts):
            print "Drawing contour #{}".format(i + 1)
            cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
            cv2.imshow("Single Contour", clone)
            cv2.waitKey(0)

        # re-clone the image and close all open windows
        clone = im.copy()
        cv2.destroyAllWindows()

        # find contours in the image, but this time keep only the EXTERNAL
        # contours in the image
        (cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
        print "Found {} EXTERNAL contours".format(len(cnts))

        # show the output image
        cv2.imshow("All Contours", clone)
        cv2.waitKey(0)

        # re-clone the image and close all open windows
        clone = im.copy()
        cv2.destroyAllWindows()

        # loop over the contours individually
        for c in cnts:
            # construct a mask by drawing only the current contour
            mask = np.zeros(gray.shape, dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)

            # show the images
            cv2.imshow("Image", im)
            cv2.imshow("Mask", mask)
            cv2.imshow("Image + Mask", cv2.bitwise_and(im, im, mask=mask))
            cv2.waitKey(0)


    def ContourMomentsAndArea(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # find external contours
        (cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        clone = im.copy()

        # loop over the contours
        for (i, c) in enumerate(cnts):
            # compute the moments of the contours which can be used to compute the
            # centroid or "center of mass" of the region.
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # draw the center of the contour on the image
            cv2.circle(clone, (cX, cY), 10, (0, 255, 0), -1)

        # show the output image
        cv2.imshow("Centroids", clone)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

        # loop over the contours again
        for (i, c) in enumerate(cnts):
            # compute the area and the perimeter of the contour
            area = cv2.contourArea(c)
            perimeter = cv2.arcLength(c, True)
            print "Contour #%d -- area: %.2f, perimeter: %.2f" %(i+1, area, perimeter)

            # draw the contour on the image
            cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)

            # compute the centre of the contour and draw contour number
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # write the area
            cv2.putText(clone, "#%d" % (i+1), (cX-20, cY), cv2.FONT_HERSHEY_SIMPLEX,
                        1.25, (255, 255, 255), 4)
            print "Centroid (%d, %d) of #%d" % (cX, cY, i+1)

        # show the output image
        cv2.imshow("Contours", clone)
        cv2.waitKey(0)

    # Shapes over the image objects
    def ShapeIt(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # find external contours
        (cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        clone = im.copy()

        # loop over the contours
        for (i, c) in enumerate(cnts):
            # fit a bounding box to the contour
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(clone, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # compute the centre of the contour and draw contour number
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # write the area
            cv2.putText(clone, "#%d" % (i+1), (cX-20, cY), cv2.FONT_HERSHEY_SIMPLEX,
                        1.25, (255, 255, 255), 4)
            print "Centroid (%d, %d, %d, %d) of #%d" % (x, y, w, h, i+1)

        # show the output image
        cv2.imshow("Bounding Boxes", clone)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        clone = im.copy()

        # loop again over the contours
        for c in cnts:
            # fit a rotated bounding box over the contour
            box = cv2.minAreaRect(c)
            box = np.int0(cv2.cv.BoxPoints(box))
            cv2.drawContours(clone, [box], -1, (0, 255, 0), 2)

        # show the output image
        cv2.imshow("Rotated Bounding Boxes", clone)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        clone = im.copy()

        # loop again
        for (i, c) in enumerate(cnts):
            # fit a minimum enclosing circle to the contour
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            cv2.circle(clone, (int(x), int(y)), int(radius), (0, 255, 0), 2)
            # compute the centre of the contour and draw contour number
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # write the area
            cv2.putText(clone, "#%d" % (i+1), (cX-20, cY), cv2.FONT_HERSHEY_SIMPLEX,
                        1.25, (255, 255, 255), 4)
            print "Centroid (%d, %d, %d) of #%d" % (x, y, radius, i+1)
        # show the output image
        cv2.imshow("Min-Enclosed Area", clone)
        cv2.waitKey(0)

        clone = im.copy()

        # loop again
        for c in cnts:
            # To fit an ellipse, contour must have atleast 5 points
            if len(c) >= 5:
                # fit the ellipse to the contour
                ellipse = cv2.fitEllipse(c)
                cv2.ellipse(clone, ellipse, (0, 255, 0), 2)

        # show the output image
        cv2.imshow("Ellipses", clone)
        cv2.waitKey(0)


    # Contour approximation
    def ContourApprox(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # find contours in the image
        (cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # loop over the contours
        for (i, c) in enumerate(cnts):
            # approximate contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.01 * peri, True)

            # if the approximation contour has 4 vertices then we are
            # examining a rectangle
            if len(approx) == 4:
                # draw the outline of the contour and write the text
                cv2.drawContours(im, [c], -1, (0, 255, 0), 2)
                (x, y, w, h) = cv2.boundingRect(approx)
                cv2.putText(im, "Rectangle", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                              0.5, (0, 255, 0), 2)

        # show the image output
        cv2.imshow("Image", im)
        cv2.waitKey(0)


    # contour sorting
    def ContourSorting(self):
        # read image
        im = cv2.imread(self.Image)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        