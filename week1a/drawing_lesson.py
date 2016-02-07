# These are my hobby project codes developed in python using OpenCV.
# Some of the projects are tested on Mac, Some on Raspberry Pi
# Anyone can use these codes without any permission
#
# Contact info: Kishwar Kumar [kumar.kishwar@gmail.com]
# Country: France
#



__author__ = 'kishwarkumar'
__date__ = '7/2/16' '9:14 PM'


# import the necessary packages
import numpy as np
import cv2

class Drawing_lesson:

    # define constructor
    def __init__(self, path):
        self.Image = path
        return

    # start drawing
    def drawit(self):
        canvas = np.zeros((300, 300, 3), dtype="uint8")

        # draw a green line from the top-left corner of our canvas to the
        # bottom-right
        green = (0, 255, 0)
        cv2.line(canvas, (0,0), (300,300), green)
        cv2.imshow("Canvas", canvas)
        cv2.waitKey(0)

        # now, draw a 3 pixel thick red line from the top-right corner to the
        # bottom-left
        red = (0, 0, 255)
        cv2.line(canvas, (300, 0), (0, 300), red, 3)
        cv2.imshow("Canvas", canvas)
        cv2.waitKey(0)

        # draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
        cv2.rectangle(canvas, (10, 10), (60, 60), green)
        cv2.imshow("Canvas", canvas)
        cv2.waitKey(0)

        # draw another rectangle, this time we'll make it red and 5 pixels thick
        cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
        cv2.imshow("Canvas", canvas)
        cv2.waitKey(0)

        # let's draw one last rectangle: blue and filled in
        blue = (255, 0, 0)
        cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
        cv2.imshow("Canvas", canvas)
        cv2.waitKey(0)

        # let's go crazy and draw 25 random circles
        for i in xrange(0, 25):
            # randomly generate a radius size between 5 and 200, generate a random
            # color, and then pick a random point on our canvas where the circle
            # will be drawn
            radius = np.random.randint(5, high=200)
            color = np.random.randint(0, high=256, size = (3,)).tolist()
            pt = np.random.randint(0, high=300, size = (2,))

            # draw our random circle
            cv2.circle(canvas, tuple(pt), radius, color, -1)

        # Show our masterpiece
        cv2.imshow("Canvas", canvas)
        cv2.waitKey(0)


        # load the image of Adrian in Florida
        image = cv2.imread(self.Image)

        # draw a circle around my face, two filled in circles covering my eyes, and
        # a rectangle surrounding my mouth
        cv2.circle(image, (168, 188), 90, (0, 0, 255), 2)
        cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
        cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
        cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)

        # show the output image
        cv2.imshow("Output", image)
        cv2.waitKey(0)